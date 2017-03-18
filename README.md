# ProxyPool
一个用于python爬虫的，抓取网上几个免费代理网站的代理池。
使用mgngodb存储，一个数据库用来存放所有爬到的IP，另一个数据库用来存放经过验证后有效的IP。
通过flask开放APi供其它的爬虫程序使用。
通过APScheduler实现每隔一段时间重新获取代理并存入数据库，并且验证代理是否可用。

# 说明
1. crawlProxy
代理池的免费代理的获取代码，通过爬取几个免费的代理网站获得免费的代理IP。

2. flask_api
代理池的对外接口，通过flask实现，提供get,getAll,delete,refresh几个API。

3. manage
代理池的管理，爬到的IP存入数据库并且验证有效后存入另一个数据库。并且定时重新获取IP后重新验证。

4. tools
代理池的配置文件和公共的函数。

# 启动方法
1. 在项目目录下使用python3 -m manage.manageProxy启动定时爬取代理及验证。
2. 在flask_api目录下使用python3 -m flask_api.flask_api启动flask的api服务就可以通过API获得代理了。

# 爬虫中使用
import requests
proxy = requests.get('http://127.0.0.1:5000/get').content

# 总结
大概完成了功能...但是需要完善的地方还有很多...有空慢慢补... 
