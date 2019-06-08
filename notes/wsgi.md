### WSGI (Web Server Gateway Interface)

- Web服务器网关接口, Python定义的一个**网关协议**
- 规定了Web Server如何与应用程序交互
- Web Server: 一个Web应用的容器 通过它可以启动应用 进而提供HTTP服务
- 应用程序: 基于框架开发的系统

### WSGI的目的

- 保证在Python中所有的Web Server程序(Gateway程序)能够通过**统一的协议**跟Web框架(Web应用)进行交互(对于部署Web程序时 可以选择任何一个实现了WSGI协议的Web Server来跑程序)
- Web应用框架只需要实现WSGI就可以跟外部请求进行交互 不用针对某个Web Server来独立开发交互逻辑