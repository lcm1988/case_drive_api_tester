#coding:utf-8
import sys
import httplib2
from time import time
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()

token_list=l=[]
suc=err=0
h=httplib2.Http()
def shopcart(myheader):
    global total,suc,err
    try:
        A,B=h.request('http://cart.srv.daling.com/api/cartnew/views','GET',headers=myheader)
        if A['status']=='200':
            suc=suc+1
    except Exception as e:
        err=err+1

try:
    if  'help' in sys.argv[1] or 'HELP' in sys.argv[1]:
        print '第一个为线程数，第二个为持续时长(分钟)'
    else:
        thread_no=int(sys.argv[1])
        keep_on_time=int(sys.argv[2])
        thread_pool = Pool(thread_no)
        fpath=r'./token.csv'

        f=open(fpath)
        for i in f:
            l=i[0:-1].split(',')
            cid,uid,tk=l[0],l[1],l[2]
            header={'clientid': cid,'accesstoken': tk,'uid': uid,'Cookie': 'clientid=%s; uid=%s; accesstoken=%s;'%(cid,uid,tk)}
            token_list.append(header)
        t1=time()
        while True:
            t2=time()
            thread_pool.map(shopcart,token_list)
            t3=time()
            if (t3-t1)/60>keep_on_time:
                break
            print 'cost is :',t3-t2
            print 'success is :',suc
            print 'error is :',err
except Exception,e:
    print e