import json
import os

from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.http import HTTPFlow


class Handler:
    def __init__(self, port, info):
        self.info = info
        self.client_request_uuid = None
        print(f'BiligameRemoveRealnameVerified(BRRV)已在端口{port}开启')

    # 请求
    def request(self, flow: HTTPFlow):
        if flow.request.url.endswith("app/v2/time/heartbeat"):
            for entry in str(flow.request.data.content)[2:-1].split("&"):
                if entry.split("=")[0].__eq__("client_request_uuid"):
                    self.client_request_uuid = entry.split("=")[1]
                    flow.request.data.headers.clear()
                    flow.request.data.content = b""

    # 响应
    def response(self, flow: HTTPFlow):
        if flow.request.url.endswith("app/v2/time/heartbeat"):
            if self.client_request_uuid is not None:
                data = json.loads("{}")
                data["code"] = "0"
                data["client_request_uuid"] = self.client_request_uuid
                data["data"] = '{"user_info":{"adult_status":1,"tour_mark":0}}'
                data["ts"] = 4
                flow.response.set_text(str(data))
                self.client_request_uuid = None
                if self.info:
                    print("取消时间更新成功")

        if str(flow.response.text).__contains__("realname_verified"):
            data = json.loads(flow.response.text)
            data["realname_verified"] = "1"  # 是否实名
            # data["remind_status"] = "1" # 实名是否有效
            flow.response.set_text(str(data))
            if self.info:
                print("实名修改成功")


def dump(options):
    server = DumpMaster(options, with_termlog=False, with_dumper=False)
    server.server = ProxyServer(ProxyConfig(options))
    return server


if __name__ == "__main__":
    config = {}

    if os.path.exists("./config.json"):
        config = json.load(open("./config.json"))

    if "host" not in config:
        config["host"] = "0.0.0.0"

    if "port" not in config:
        config["port"] = 25560

    if "info" not in config:
        config["info"] = True

    f = open("./config.json", "w")
    f.write(json.dumps(config))
    f.close()

    master = dump(
        Options(listen_host=config["host"], listen_port=config["port"], http2=False, ssl_insecure=True))
    master.addons.add(Handler(config["port"], config["info"]))
    master.run()
