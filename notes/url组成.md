URL是Uniform Resource LocatorF的简写，统一资源定位符。

一个URL由以下几部分组成

```python
scheme://host:post/path/?query-string=xxx#anchor
```

* scheme: 代表的是访问的协议，一般为http或者https以及ftp等.
* host: 主机名, 域名. 比如: www.baidu.com
* port: 端口号. 访问某一个网站的时候, 浏览器默认使用80端口.
* path: 查找路径. 比如: www.jianshu.com/trending/now, 后面的trending/now就是path.
* query-string: 查询字符串, 比如: www.baidu.com/s?wd=python, wd=python就是查询字符串.
* anchor: 锚点, 前端用来定位. 比如: https://baike.baidu.com/item/刘德华/114923?fr=aladdin#4.