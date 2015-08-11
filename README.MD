# PostBaiduSitemap
百度链接提交

实现 百度站长 - 网页抓取 - 链接提交 - 主动提交(实时) 的功能。

具体可参看 [百度站长](http://zhanzhang.baidu.com/linksubmit/)。

# 使用方法

在 main.py 中的

`urlSitemap` 填写你的Sitemap地址，形如 'http://blog.kxrr.us/index.php/sitemap'

`urlPost` 填写你的百度接口地址， 形如 'http://data.zz.baidu.com/urls?site=blog.kxrr.us&token=xxxxxxxxxxxx'

然后运行 `python main.py`。 可以在VPS中设置定时任务。

# 实现功能
主动推送，目前为分条推送。

一条URL推送成功后，将保存在 _urlPosted.txt 中，第二次运行将不再推送。

可根据自己的博客更新周期设置定时任务的周期。