#coding: utf-8
import time
import sys

import pycurl,StringIO
b = StringIO.StringIO()
c = pycurl.Curl()
c.setopt(pycurl.PROXY, 'http://127.0.0.1:8888')
c.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")
c.setopt(pycurl.URL, 'http://www.baidu.com')
#c.setopt(pycurl.WRITEFUNCTION, sys.stderr.write)

begin=time.time()
for i in range(50):
    c.perform()
    print c.getinfo(pycurl.HTTP_CODE)
end=time.time()
print end-begin
#16.0149998665