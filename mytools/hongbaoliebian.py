#coding:utf-8
from tools.header_tools import headertools
from tools.http_connercter import http2
from json import loads

h=http2()
#分享获取红包,只为并发，不打印响应
def get_order_coupon(targs=()):
    url='http://m.ymall.com/api/share/index?share_type=orderDetailEnvelopes&share_to=24&order_sn='+targs[0]+'&bda_id=2&web_url=http://wxbeta.daling.com/activity/coupon/index.html?id=2&t='+targs[0]+'&t='+targs[0]
    A,B=h.conn(url,'GET',header=targs[1])
    #B=loads(B)
    #print B

#领取红包,只为并发，不打印响应
def get_share_coupon(targs=()):
    url='http://wxbeta.daling.com/api/bdactivity/index?id=2&t='+targs[0]
    A,B=h.conn(url,'GET',header=targs[1])
    #B=loads(B)
    #print B

if __name__=='__main__':
    from gevent.pool import Pool
    from gevent import monkey
    monkey.patch_all()
    pool = Pool(40)

    #cachefile1='./cache1'
    #myheader1=headertools().loadHeader(cachefile1)
    #order_sn='963296110000001'
    #myargs=[(order_sn,myheader1)]*80
    #pool.map(get_order_coupon,myargs)

    cachefile2='./cache2'
    myheader2=headertools().loadHeader(cachefile2)
    order_sn='963296110000001'
    myargs=[(order_sn,myheader2)]*80
    pool.map(get_share_coupon,myargs)
