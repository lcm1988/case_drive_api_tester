#coding: utf-8
from tools.header_tools import headertools
from usercenter import usercenter
from json import loads
from time import sleep
import hashlib
import httplib2
import redis

#MD5加密
def md5code(mystr):
    md= hashlib.md5()
    md.update(mystr)
    return md.hexdigest()

#红包雨首页
def get_index(myheader):
    h=httplib2.Http(proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, 'localhost', 8888))
    A,B=h.request('http://wxbeta.daling.com/activity/api/lottery/index','GET',headers=myheader)
    #B=loads(B)
    return B

#红包雨开始
def get_token(myheader):
    h=httplib2.Http(proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, 'localhost', 8888))
    A,B=h.request('http://wxbeta.daling.com/activity/api/lottery/start','GET',headers=myheader)
    B=loads(B)
    try:
        return B['data']['token']
    except Exception,e:
        return 'err'

#红包雨结束
def get_luck(args=()):
    h=httplib2.Http(proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, 'localhost', 8888))
    A,B=h.request('http://wxbeta.daling.com/activity/api/lottery/getLuck?t='+str(args[0]),'GET',headers=args[1])
    #B=loads(B)
    return B
    #return B['data']['amount']

#红包雨分享页
def get_share(mobile):
    h=httplib2.Http(proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, 'localhost', 8888))
    A,B=h.request('http://wxbeta.daling.com/activity/api/lottery/getShare?t='+md5code(mobile),'GET')
    #B=loads(B)
    return B

#红包领取
def get_shareluck(args=()):
    h=httplib2.Http(proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, 'localhost', 8888))
    A,B=h.request('http://wxbeta.daling.com/activity/api/lottery/getShareLuck?t='+md5code(args[0]),'GET',headers=args[1])
    #B=loads(B)
    return B

if __name__=="__main__":
    from gevent.pool import Pool
    from gevent import monkey
    monkey.patch_all()
    thread_pool = Pool(50)

    rds_pool=redis.ConnectionPool(host='10.36.4.66',port=6379)
    rds=redis.Redis(connection_pool=rds_pool)
    cachefile="cache2"
    header=headertools().loadHeader(cachefile)

    #新客17720000001
    #header['UID']='15015126'
    #header['ACCESSTOKEN']='d40fbcdd60f55c6b862a33c97c7cac25_2_1'
    #组装cookies
    header['COOKIE']='uid=%s;accesstoken=%s'%(header['UID'],header['ACCESSTOKEN'])

    #红包首页
    print  get_index(header)

    #抢红包
    for i in range(3):
        #第二次获得188大红包
        if i==2:
            rds.setex('hongbaoyu_total_1480593601_play_cnt',1211,86400)
        t=get_token(header)
        targs=[(t,header)]*40
        sleep(15)
        thread_pool.map(get_luck,targs)
    #print get_luck(t,header)
##
    t=get_token(header)
    print t
    print get_luck((t,header))
    #rstr=['hongbaoyu_'+md5code('18810192825')+'_list','hongbaoyu_total_1480593601_play_cnt','hongbaoyu_total_1480593601']
    #print [rds.get(i) for i in rstr]

    #分享页面
    #print get_share('18810192825')

    #领取红包
    #targs=[('18810192825',header)]*100
    #thread_pool.map(get_shareluck,targs)
    #rstr= ['hongbaoyu_'+md5code('17720000001')+'_list','hongbaoyu_'+md5code('18810192825')+'_list']
    #print [rds.get(i) for i in rstr]

    #定时queen
    #rds.rpush('lottery_task_queue','{"user_id":15015054,"user_name":"18810192825","amount":104,"ctime":1478606787,"type":1,"utime":1478606806}')
    #print rds.rpop('lottery_task_queue')
