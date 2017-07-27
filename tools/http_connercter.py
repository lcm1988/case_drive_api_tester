#coding:utf-8
from conf.config import POXY_HOST,POXY_PORT
class http2():
    def __init__(self):
        pass

    #通过代理访问指定请求并返回请求结果
    def conn(self,url='',method='GET',para='',header={},host=POXY_HOST,port=POXY_PORT):
        import httplib2
        if host is not None and port is not None:
            h = httplib2.Http(proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, host, int(port)))
        else:
            h=httplib2.Http()
        if method.upper()=='GET':
                A,B=h.request(url,'GET',headers=header) if header else h.request(url,'GET')
        elif method.upper()=='POST':
            if para:
                A,B=h.request(url,'POST',para,header) if header else h.request(url,'POST',para)
            else:
                raise ValueError,'Para must be gaven when method is POST'
        return A,B

    #通过代理进行文件上传，并返回请求结果
    #para格式：{"arg1":"arg1","file1": open(r"F:\111.png", "rb")}
    def file_transer(self,url='',para={},header={},host=POXY_HOST,port=POXY_PORT):
        import urllib2
        import gzip
        import StringIO
        from poster.encode import multipart_encode
        from poster.streaminghttp import register_openers
        if host is not None and port is not None:
            proxy_handler = urllib2.ProxyHandler({'http':'%s:%s'%(sock['host'],str(sock['port']))})
            opener = urllib2.build_opener(proxy_handler)
            urllib2.install_opener(opener)
        else:
            null_proxy_handler = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(null_proxy_handler)
            urllib2.install_opener(opener)
        register_openers()
        a,b = multipart_encode(para)
        header['Content-Length']=b['Content-Length']
        header['Content-Type']=b['Content-Type']
        try:
            req = urllib2.Request(url,a,header)
            result=urllib2.urlopen(req)
            #判断是否压缩报文
            if result.info().get('Content-Encoding', "") == 'gzip':
                buf = StringIO.StringIO(result.read())
                res=gzip.GzipFile(fileobj=buf)
                res=res.read()
            else:
                res=result.read()
            return res
        except Exception as e:
            print e

if __name__=="__main__":
    from urllib import urlencode
    a=http2()
    #print a.conn('http://www.baidu.com')[0]
    dl_header={'Host': 'www.daling.com',
           'Connection': 'keep-alive',
           'Accept': '*/*',
           'Origin': 'http://www.daling.com',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Referer': 'http://www.daling.com/index.php?_c=login&_a=index',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Pragma': 'no-cache'}
    c={'url':'http://www.daling.com/index.php?_c=login&_a=login','method':'POST','para':{'mobile':'18810192825','pass':'123456'},'header':dl_header}
    print c.keys()
    print a.conn(c['url'],c['method'],para=urlencode(c['para']),header=c['header'],host='localhost',port=8888)[1]
