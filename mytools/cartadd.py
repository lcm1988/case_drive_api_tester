#coding: utf-8
from tools.header_tools import headertools
from tools.http_connercter import http2
from urllib import urlencode
from json import loads
import

#加入购物车方法
def cart_add(data,header):
    a=http2()
    for i in range(0,len(data)):
        para={'gid':str(data[i])}
        para=urlencode(para)
        try:
            A,B=a.conn('http://m.ymall.com/api/cartnew/add?'+para,"GET",header=header)
            B=loads(B)
            if (B["status"]=="200" and B["data"]["msg"]==u"添加成功!"):
                print "添加成功"
            else:
                print "添加失败"
        except Exception as e:
            print "添加失败",e

if __name__=="__main__":
   cachefile="cache1"
   try:
       #data=[237678,159977]
       #myheader=headertools().loadHeader(cachefile)
       #cart_add(data,myheader)
       from usercenter import user
       test=http2()
       client=user()
       client.header['APPVERSION']="5.9.2"
       myheader= client.get_client_header('20161121001')
       print myheader
       A,B=test.conn('http://a.app.beta.daling.com/channel/index?channel_id=1','GET',header=myheader)
       print B
       #print user().get_usertab(15003095)
   except Exception as e:
       print e


