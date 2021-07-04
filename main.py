import json
import os

from mitmproxy.addons import export
from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.tools.web.master import WebMaster
from mitmproxy.tools.console.master import ConsoleMaster
from mitmproxy.http import HTTPFlow
from mitmproxy import master, ctx, http


class fcm:
    def __init__(self):
        print('BiligameRemoveRealnameVerified(BRRV)已在端口25560开启')

    def response(self, flow: HTTPFlow):
        if flow.response.text.endswith(".jpg"):
            return

        if str(flow.response.text).__contains__("realname_verified"):
            data = json.loads(flow.response.text)
            data["remind_status"] = "1"
            flow.response.set_text(str(data))


def run_dump(options):
    server = DumpMaster(options, with_termlog=False, with_dumper=False)
    server.server = ProxyServer(ProxyConfig(options))
    return server

if __name__ == "__main__":
    master = run_dump(Options(listen_host='0.0.0.0', listen_port=25560, http2=False, ssl_insecure=True))
    master.addons.add(fcm())
    master.run()
