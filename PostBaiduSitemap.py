#-*- coding: utf-8 -*-
import requests
import re

__Author__ = 'Kxrr'
__Verson__ = 0.1

class Pbs(object):
    def __init__(self, urlSitemap, urlPost):
        self.urlSitemap = urlSitemap
        self.urlPost = urlPost
        self.HEADERS_POST = {
            "User-Agent": "curl/7.12.1",
            "Host": "data.zz.baidu.com",
            "Content-Type": "text/plain",
            "Content-Length": "83"
        }
        self.f = open('_urlPosted.txt', 'a+')
        self.fContent = self.f.read()
        self.f.close()

    def getSitemap(self):
        self.responseSitemap = requests.get(self.urlSitemap)
        self.listSitemap = re.findall('<loc>(.*?)</loc>', self.responseSitemap.content, re.S)

    def sortList(self):
        self.g = open('_urlPosted.txt', 'a+')

    def postSitemap(self):
        for self.eachUrl in self.listSitemap:
            if self.eachUrl in self.fContent:
                pass
            else:
                self.responsePost = requests.post(self.urlPost, data=self.eachUrl, headers=self.HEADERS_POST)
                if '"success":1' in self.responsePost.content:
                    self.g.write(self.eachUrl + '\n')
                    print self.eachUrl + ' Done.'
        self.g.close()

    def run(self):
        self.getSitemap()
        self.sortList()
        self.postSitemap()

