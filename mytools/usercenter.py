#coding:utf-8
import hashlib
import uuid
import httplib2
from urllib import urlencode
from json import loads
from time import time

PASSPORT_URL='http://a.passport.corp.daling.com'

h=httplib2.Http(proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, 'localhost', 8888))
#定义鉴权中心方法
class usercenter():
    def __init__(self):
        #初始化鉴权中心后台接口地址
        self.passport_url=PASSPORT_URL

    #定义utf8转码方法
    def utf8(self,value):
        #基础类型定义
        _UTF8_TYPES = (bytes, type(None))
        if not isinstance(b'', type('')):
            unicode_type = str
            basestring_type = str
        else:
            unicode_type = unicode
            basestring_type = basestring
        #转码操作
        if isinstance(value, _UTF8_TYPES):
            return value
        if not isinstance(value, unicode_type):
            raise TypeError("Expected bytes, unicode, or None; got %r" % type(value))
        return value.encode("utf-8")

    #获取用户分表信息，用于确定dl_user_XX表和dl_user_info_XX表的分表
    def get_usertab(self,u_id):
        user_sn = hashlib.md5(str(u_id)).hexdigest()
        return user_sn[0]

    #获取设备分表信息，用于确定dl_device_XX表的分表
    def get_devicetab(self,*parts):
        APPSN_DNS_SUFFIX = 'GZ7#c3Ut_bAB@B5Z59vhvcvhmFDM?MmG.app.pp.dl.com'
        s = '.'.join(parts)
        dns_key = '%s.%s' % (self.utf8(s), APPSN_DNS_SUFFIX)
        res= uuid.uuid5(uuid.NAMESPACE_DNS, dns_key).hex
        return res[0]

    #获取设备验签，在init文件中进行了重命名
    def get_finger(self,*parts):
        secret='lc@Q#HN_LvI_C4mkaABW95N%397d31vT6ZaLBh0AtfpV7V8sF6uIRLteOJIckz$'
        secret = self.utf8(secret)
        s      = self.utf8(''.join(parts))
        message = '%s%s' % (secret, s)
        return hashlib.md5(message).hexdigest()

    def check_header(self,header):
        if header:
            queryid=int(time())
            deviceVersion=userVersion="v2"
            url = "/api/" +deviceVersion+"/auth/compat/app/device"
            status="DEVICE"
            if 'uid' in header.keys() or 'UID' in header.keys():
                url= "/api/" +userVersion +"/auth/compat/app?uid="+header["UID"]+"&access_token="+header["ACCESSTOKEN"]+"&queryid="+str(queryid)
                status="USER"
            url=self.passport_url+url

            url_header={}
            url_header['DLTOKEN'] = header['DLTOKEN']
            url_header['DLFINGERPRINT'] = header['DLFINGER']
            url_header['CLIENTID'] = header['CLIENTID']
            url_header['DEVICEMODE'] = header['DEVICEMODE']
            url_header['DEVICESIZE'] = header['DEVICESIZE']
            url_header['SYSTEMVERSION'] = header['SYSTEMVERSION']
            url_header['PLATFORM'] = header['PLATFORM']
            url_header['APPNAME'] = header['APPNAME']
            url_header['APPVERSION'] = header['APPVERSION']
            url_header['CHANNELID'] = header['CHANNELID']

            A,B=h.request(url,"GET",headers=url_header)
            B=loads(B)
            try:
                if status=="DEVICE" and B["data"]["device"]["app_name"]:
                    return True
                elif status=="USER" and B["data"]["user"]["is_login"]:
                    return True
                else:
                    return False
            except Exception as e:
                print e
                return False
        else:
            print "无效的header信息"
            return False

    #通过用户id查询用户信息
    def get_user_by_id(self,uid):
        url=self.passport_url+"/api/v1.2/users/"+str(uid)
        try:
            A,B=h.request(url,"GET")
            B=loads(B)
            if B["msg"]=="SUCCESS":
                return B
            else:
                print B["msg"]
                return False
        except Exception as e:
            return False

    #通过手机号查询用户信息
    def get_user_by_name(self,mobile):
        para={"user_name":mobile}
        url=self.passport_url+"/api/v1.1/users/byname"
        url=url+"?"+urlencode(para)
        try:
            A,B=h.request(url,"GET")
            B=loads(B)
            if B["msg"]=="SUCCESS":
                return B
            else:
                print B["msg"]
                return False
        except Exception as e:
            return False


class user(usercenter):
    def __init__(self,header={}):
        if header:
            self.header=self.init_header=header
        else:
            self.header=self.init_header={"DEVICEMODE": "HUAWEI G750-T20",
                         "charsert": "utf-8",
                         "CHANNELID": "009",
                         "ham": "WIFI",
                         "APPNAME": "com.daling.daling",
                         "DLFINGER": "",
                         "DEVICESIZE": "1080*1920",
                         "APPVERSION": "5.6.5",
                         "User-Agent": "Dalvik/1.6.0 (Linux; U; Android 4.2.2; HUAWEI G750-T20 Build/HuaweiG750-T20)",
                         "DLTOKEN": "00000000-0000-0000-0000-000000000000",
                         "PLATFORM": "android",
                         "Connection": "Close",
                         "SYSTEMVERSION": "4.2.2",
                         "Pragma": "no-cache",
                         "CHANNELNAME": "???",
                         "Content-Type": "application/x-www-form-urlencoded",
                         "Accept-Encoding": "gzip"}

    def get_client_header(self,client_id):
        reg_header=self.init_header
        reg_header["CLIENTID"]=str(client_id)
        #顺序:client_id,device_mode,platform,app_name,app_version
        reg_finger=self.get_finger(reg_header["CLIENTID"],reg_header["DEVICEMODE"],reg_header["PLATFORM"],reg_header["APPNAME"],reg_header["APPVERSION"])
        print reg_finger
        reg_url="http://passport.daling.com/api/v1/tokens?dl_fingerprint="+reg_finger
        reg_para={"IDFV":"",
                  "IDFA":"",
                  "MAC":"",
                  "UID":"",
                  "APPVERSION":reg_header["APPVERSION"],
                  "CLIENTID":reg_header["CLIENTID"],
                  "PLATFORM":reg_header["PLATFORM"],
                  "DEVICEMODE":reg_header["DEVICEMODE"],
                  "APPNAME":reg_header["APPNAME"],
                  "SYSTEMVERSION":reg_header["SYSTEMVERSION"],
                  "DEVICESIZE":reg_header["DEVICESIZE"],
                  "CHANNELID":reg_header["CHANNELID"]}
        reg_body=urlencode(reg_para)
        try:
            A,B=h.request(reg_url,"POST",reg_body,reg_header)
            B=loads(B)
            #如果结果正确，加载登录相关字段并返回整个header
            if A['status']=="200" and str(B['status'])=="200":
                reg_header["DLTOKEN"]=B["data"]["dl_token"]
                reg_header["DLFINGER"]=B["data"]["dl_fingerprint"]
            else:
                reg_header={}
        except Exception as e:
            print e
            reg_header={}
        self.header=reg_header
        return self.header

    #注册设备后登录，并返回完整的header
    def get_user_header(self,u_name,u_pwd,client_id):
        log_header=self.get_client_header(client_id)
        #print log_header
        log_url="http://m.ymall.com/api/user/login"
        log_para={"user_name":u_name,"pass":u_pwd}
        log_body=urlencode(log_para)
        try:
            A,B=h.request(log_url,"POST",log_body,log_header)
            B=loads(B)
            #如果结果正确，加载登录相关字段并返回整个header
            if A['status']=="200" and str(B['status'])=="200":
                log_header['UID']=B["data"]["uid"]
                log_header['ACCESSTOKEN']=B["data"]["accesstoken"]
                log_header['DLTOKEN']=B["data"]["token"]["dl_token"]
                log_header['DLFINGER']=B["data"]["token"]["dl_fingerprint"]
            #如果结果错误，将header置空，便于跟踪错误
            else:
                log_header={}
        except Exception as e:
            print e
            log_header={}
        self.header=log_header
        return self.header

if __name__=="__main__":
    #usercenter=usercenter()
    #print usercenter.get_user_by_name('18810192825')
    #user=user()
    #print user().get_client_header('20160525005')
    #user.get_user_header('18810192825','123456','20160525005')
    #print usercenter().check_header(user().get_client_header('20160525005'))
    #print usercenter().get_usertab(8144681)
    #print usercenter().get_usertab(6987261)
    #print usercenter().get_usertab(7480717)
    l='abdcdeajdflasdkfjha\r\n'
    print '1',l[-3:],'2'
