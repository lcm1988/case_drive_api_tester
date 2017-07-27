#coding:utf-8
from psycopg2 import connect as conn,extras
import memcache
import json
import httplib2

def setwallet(mobile,env,money=999999):
    try:
        #加载配置
        if env.upper() in ('A','B','C','D'):
            uc_path='http://%s.passport.corp.daling.com/api/v1.1/users/byname?user_name='%env.lower()+str(mobile)
            db_name='dal_mbr_wallet_beta%s'%env.upper()
            db_conf={'host':'10.36.2.22','port':'5432','usr':'pgsql','pwd':'pgsql','db':db_name}
            mem_conf={'A':'10.36.4.66:4444','B':'10.36.4.66:7777','C':'10.36.4.66:8888','D':'10.36.4.66:5555'}[env.upper()]
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

        #修改数据库
        sql="update \"member\" set total_money=%s where id=%s"%(money,uid)
        pg=conn(host=db_conf['host'], port=db_conf['port'], user=db_conf['usr'], password=db_conf['pwd'], database=db_conf['db'])
        cursor=pg.cursor(cursor_factory=extras.DictCursor)
        cursor.execute(sql)
        pg.commit()
        cursor.close()
        pg.close()

        #清空memcache
        mem=memcache.Client([mem_conf])
        mem.flush_all()

        print '更新成功'
    except Exception,e:
        print e

if __name__=="__main__":
    #应用举例
    setwallet(18810192825,'b')#更新成功
    #setwallet(18612481280,'a')#更新成功
    #setwallet(188101928251,'e')#Wrong properties
    #setwallet(188101928251,'a')#Wrong mobile