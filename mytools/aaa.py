#coding:utf-8
import httplib2
import json
from tools.data_compare import datacompare

url="https://passport.huajiao.com/user/login?userid=0&deviceid=91e661bac2f8373d16994da8716afc0d&platform=ios&network=wifi&version=2.7.0&rand=1319992778&netspeed=0&time=1494840258&guid=caaebf199c66f592f71ac1b9aeb7c4f0&token=&appname=camera"
h = httplib2.Http(".cache",proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, 'localhost',8888))

h.add_credentials('name', 'password')
(resp, content) = h.request(url,
                            "POST", body="mobile=%2B8618810192825&password=25d55ad283aa400af464c76d713c07ad",
                            headers={'content-type':'application/x-www-form-urlencoded'} )
content=json.loads(content)

expect_json={"data":{"nickname":"右手_天堂"}}
print content['errmsg']
l=datacompare(expect_json,content)
print l
