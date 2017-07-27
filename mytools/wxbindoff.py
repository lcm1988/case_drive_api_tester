#coding:utf-8
from psycopg2 import connect as conn,extras
import hashlib
import json
import httplib2

def wxbindoff(mobile,env):
    try:
        #加载配置
        if env.upper() in ('A','B','C','D'):
            uc_path='http://%s.passport.corp.daling.com/api/v1.1/users/byname?user_name='%env.lower()+str(mobile)
            db_name='uc_beta_%s'%env.lower()
            db_conf={'host':'10.36.2.22','port':'5432','usr':'pgsql','pwd':'pgsql','db':db_name}
        else:
            raise ValueError,'Wrong properties'

        #获取用户id
        h=httplib2.Http(proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, 'localhost', 8888))
        A,B=h.request(uc_path,'GET')
        B=json.loads(B)
        if 'user_id' in B['data'].keys():
            uid=B['data']['user_id']
        else:
            raise ValueError,'Wrong mobile'

        #获取用户分表信息
        user_tab=hashlib.md5(str(uid)).hexdigest()[0]
        print uid,user_tab
        #修改数据库
        sql="delete from dl_user_weixin_%s where u_id=%s"%(user_tab,uid)
        pg=conn(host=db_conf['host'], port=db_conf['port'], user=db_conf['usr'], password=db_conf['pwd'], database=db_conf['db'])
        cursor=pg.cursor(cursor_factory=extras.DictCursor)
        cursor.execute(sql)
        pg.commit()
        cursor.close()
        pg.close()

        print '解绑成功'
    except Exception,e:
        print e

if __name__=="__main__":
    #应用举例
    wxbindoff(18611131363,'a')#解绑成功
    #wxbindoff(188101928251,'e')#Wrong properties
    #wxbindoff(188101928251,'a')#Wrong mobile