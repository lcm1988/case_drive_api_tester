#coding:utf-8
import httplib2
import json
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()
thread_pool = Pool(5)

#源文件数据、源文件行、目标文件数据
f_list=l_list=res_list=[]

#接口获取用户token
def gettoken(uid):
    pass_uri='http://passport.srv.daling.com/api/v2/users/%s'%uid
    #h=httplib2.Http()
    h=httplib2.Http()
    A,B=h.request(pass_uri,'GET')
    B=json.loads(B)
    return B['data']['token']

#根据每行数据拼出目标数据list
def makeline(line):
    global res_list
    try:
        res_list.append(line[0],line[1],gettoken(line[1]))
    except Exception,e:
        print e

#生成源文件数据
f=open(r'F:\cart.csv')
for line in f:
    #l_list=line[0:-1].strip('"').split('","')
    if line[-1:]=='\n':
        if line[-2:]=='\r\n':
            l_list=line[0:-2].strip('"').split('","')
        else:
            l_list=line[0:-1].strip('"').split('","')
    f_list.append(l_list)

print f_list
#生成目标文件数据
#thread_pool.map(makeline,f_list)
print res_list

#写入文件
fp=open(r'F:\token.csv','w')
for i in res_list:
    line=','.join(i)+'\n'
    fp.write(line)
fp.close()

print gettoken(17445368)