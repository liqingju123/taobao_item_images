# encoding:utf-8
from urllib import urlopen
import urllib2 
import re
from pip._vendor import requests


# 淘宝使用的是 https 使用HTTPS 请求
def _ssl_get_images_(ssl_host):
    requ = requests.get('https:%s' % ssl_host, verify=False)
    return requ.text
print _ssl_get_images_('//detail.tmall.com/item.htm?id=536654834960&ali_trackid=17_ed65d6e3328e95d1a9ac1bf48af3fc16&spm=a21bo.50862.201862-4.1.UbFuna')