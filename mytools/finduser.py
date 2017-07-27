#coding:utf-8
import httplib2
import json


#接口获取用户token
def gettoken(uid):
    pass_uri='http://passport.srv.daling.com/api/v2/users/%s'%uid
    #h=httplib2.Http()
    h=httplib2.Http()
    A,B=h.request(pass_uri,'GET')
    B=json.loads(B)
    return B['data']['ctime'],B['data']['uuid'],B['data']['user_name']

f=open(r'f:\ym_lottery_reward.csv')
list=[]

for i in f:
    uid= i[0:-1].strip('"')
    ctime=gettoken(uid)
    if ctime[0] > 1488384000:
        print str(uid),ctime
    else:
        continue
'''
print len(list)
fp=open(r'F:\token.csv','w')
for i in list:
    fp.write(i)
fp.close()
'''