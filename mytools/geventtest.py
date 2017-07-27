#coding:utf-8
import multiprocessing
import time
import os
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()


err=0
f=open(r'f:\test.txt','a+')
def writefile(tstring):
    global err,f
    try:
        #f=open(r'f:\test.txt','a+')
        f.write(tstring+''+str(time.time())+'\n')
        #f.close()
    except Exception,e:
        err=err+1

def dowork(t,arglist=[]):
    t_pool=Pool(t)
    a=time.time()
    t_pool.map(writefile,arglist)
    f.close()
    b=time.time()
    s= float(b-a)
    return float(s/t)


def worker(arglist):
    print 'worker started'
    s=dowork(arglist)
    print 'sleeped %ss worker ended'%str(s)


if __name__=="__main__":
    l1=['a']*50000
    l2=['b']*50000
    l3=['c']*50000
    l4=['d']*50000
    #t1=time.time()
    '''
    p1= multiprocessing.Process(target=worker,args=(l1,))
    p2= multiprocessing.Process(target=worker,args=(l2,))
    p3= multiprocessing.Process(target=worker,args=(l3,))
    p4= multiprocessing.Process(target=worker,args=(l4,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print "END!!!!!!!!!!!!!!!!!"
    #t2=time.time()
    #print float(t2-t1)
    '''
    l5=l1+l2+l3+l4

    print dowork(100,l5)
    os.system('del /F f:\test.txt')

    print err