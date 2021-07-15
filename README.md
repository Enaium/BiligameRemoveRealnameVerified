# BiligameRemoveRealnameVerified B站游戏实名验证移除

安装mitmproxy `pip install mitmproxy`

Python运行`main.py`

手动代理 ip为电脑的IPv4地址 打开连接属性可看到 端口为运行后的提示的端口

[![RfTxC4.png](https://z3.ax1x.com/2021/07/04/RfTxC4.png)](https://imgtu.com/i/RfTxC4)

访问 http://mitm.it/ 安装证书【可以不安装但是https访问会访问不了】

## 取消实名 ⚠登录后可关闭

启动游戏登录***⚠90分钟禁止进入游戏的可能不行***

[![Rh5udS.png](https://z3.ax1x.com/2021/07/05/Rh5udS.png)](https://imgtu.com/i/Rh5udS)

会提示你实名无效

随便生成个填进去

[![Rh5lGj.png](https://z3.ax1x.com/2021/07/05/Rh5lGj.png)](https://imgtu.com/i/Rh5lGj)

之后进入游戏

访问 https://my.biligame.com/smz/ 查看是否有没实名

[![Rf7aMn.png](https://z3.ax1x.com/2021/07/04/Rf7aMn.png)](https://imgtu.com/i/Rf7aMn)

如果重新打开游戏提示要实名

[![R4sECV.png](https://z3.ax1x.com/2021/07/05/R4sECV.png)](https://imgtu.com/i/R4sECV)

每次登录开着工具

大概持续24小时会恢复 再次重复步骤即(提前查看是否有实名验证,以防90分钟禁止进入游戏)

## 取消时间限制(记录时间) ⚠需要一直开着

此工具也提供了取消时间限制

## 配置

默认配置

```json
{
  "host": "0.0.0.0",
  "port": 25560,
  "info": true
}
```



只试了碧蓝航线

关键字:B站游戏 BiliBili游戏 实名认证 防沉迷
