#-*- coding: utf-8 -*-

from PostBaiduSitemap import Pbs

urlSitemap = '' # Your sitemap url, like 'http://blog.kxrr.us/index.php/sitemap'
urlPost = '' # Your Baidu sitemap API, like 'http://data.zz.baidu.com/urls?site=blog.kxrr.us&token=xxxxxxxxxxxx'

if __name__ == '__main__':
    pbs = Pbs(urlSitemap,urlPost)
    pbs.run()