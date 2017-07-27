#coding:utf-8
#加载http请求类、xml&dict转换类、请求头读取/保存类、数据对比方法
from tools import http2,xmltransfer,headertools,datacompare,testlogger,htmlreporter
#加载urlencode方法
from urllib import urlencode
#加载字符串转换字典方法
from json import loads
from time import time
from os import getcwd

#协程处理
from conf.config import THREAD_NUM
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()
# 线程数
pool = Pool(THREAD_NUM)#放入线程池执行

#日志路径
logpath=getcwd()+r'/result/gtestlog'+str(int(time()))+'.log'
logger=testlogger(logpath)

case_html_output=[]
pass_no=fail_no=err_no=0

#协程原子方法,因线程处理写log消耗资源较大，此不进行log写操作
def runcase(atomic_case={}):
    global case_html_output,pass_no,fail_no,err_no,logger
    res_list=[]
    res_flag=None
    try:
        #判断为get请求
        if atomic_case['method'].upper()=='GET':
            #判断case中有无请求头，有则带请求头发送
            a,b=http2().conn(url=atomic_case['url'],header=atomic_case['header']) if 'header' in atomic_case.keys() else http2().conn(url=atomic_case['url'])

        #判断为post请求
        elif atomic_case['method'].upper()=='POST':
            #判断para为字典类型，进行urlencode后发送
            if isinstance(atomic_case['para'],dict):
                #判断case中有无请求头，有则带请求头发送
                a,b=http2().conn(atomic_case['url'],atomic_case['method'],urlencode(atomic_case['para']),atomic_case['header']) if 'header' in atomic_case.keys() else http2().conn(atomic_case['url'],atomic_case['method'],urlencode(atomic_case['para']))
            #判断para为字符串，直接发送
            elif isinstance(atomic_case['para'],(str,basestring,unicode)):
                #判断case中有无请求头，有则带请求头发送
                a,b=http2().conn(atomic_case['url'],atomic_case['method'],atomic_case['para'],atomic_case['header']) if 'header' in atomic_case.keys() else http2().conn(atomic_case['url'],atomic_case['method'],atomic_case['para'])

        #加入预期expect_json,与实际结果比对
        b=loads(b)
        res_list=datacompare(atomic_case['expect_json'],b,'节点:',[])

        if not len(res_list):
            pass_no+=1
            res_flag=1
            logger.writelog(atomic_case['case_name']+'与预期数据匹配一致,测试通过')
        else:
            fail_no+=1
            res_flag=0
            logger.writelog(atomic_case['case_name']+'与预期数据匹配不一致,测试失败,对比结果如下：'+'\n'+'\t'+'\n\t'.join(res_list))

    #执行异常后打印异常
    except Exception,e:
        err_no+=1
        res_flag=2
        res_list.append('执行异常:'+str(Exception)+str(e))
        logger.writelog('-'*50+'ERROR'+'-'*50+'\n'+atomic_case['case_name']+'执行异常:'+str(Exception)+str(e)+'\n'+'-'*50+'ERROR'+'-'*50)

    finally:
        #替换掉左右尖括号
        for idx1,val1 in enumerate(res_list):
            res_list[idx1]=val1.replace('<','&lt;').replace('>','&gt;')
        res_list='<br>'.join(res_list) if len(res_list) else '暂无信息'
        #收录进case_html_output以备生成html
        case_html_output.append([atomic_case['case_name'],atomic_case['case_content'],res_flag,res_list])

#主方法
def main():
    #开始时间
    time_start=time()
    global case_html_output,pass_no,fail_no,err_no,logger
    try:
        #导入case文件
        from case_demo import case
        #校验case是否合法
        case_err=False
        logger.writelog('开始校验case数据合法性：')
        for idx,vals in enumerate(case):
            if 'url' not in vals.keys():
                case_err=True
                logger.writelog('第'+str(idx+1)+'行用例错误：url不能为空')

            if 'method' in vals.keys():
                if vals['method'].upper() not in ('POST','GET'):
                    case_err=True
                    logger.writelog('第'+str(idx+1)+'行用例错误：不支持的method方法')

                elif vals['method'].upper() =='POST':
                    if 'para' not in vals.keys():
                        case_err=True
                        logger.writelog('第'+str(idx+1)+'行用例错误：POST方法必须给出参数')

                    elif len(vals['para'])==0:
                        case_err=True
                        logger.writelog('第'+str(idx+1)+'行用例错误：POST方法参数不能为空')
            else:
                case_err=True
                logger.writelog('第'+str(idx+1)+'行用例错误：method方法不能为空')

            if 'header' in vals.keys():
                if not isinstance(vals['header'],dict):
                    case_err=True
                    logger.writelog('第'+str(idx+1)+'行用例错误：header必须为dict')

        #如果用例数据错误则抛出异常，流程终止
        if case_err:
            raise ValueError,u'wrong case,test cancled'
        else:
            logger.writelog('case合法性校验通过，开始执行自动化测试:\n'+'#'*50+'协程处理暂不打印log日志'+'#'*50)

        #多线程运行，运行结果存储进case_html_output
        pool.map(runcase,case)

    except Exception as e:
        logger.writelog(str(e))
        #print e

    time_end=time()
    time_cost=time_end-time_start
    print '执行耗时',time_cost,'秒'
    #写入统计参数
    logger.writelog('\n')
    logger.writelog('测试完毕，通过用例数：'+str(pass_no)+'，失败用例数：'+str(fail_no)+'，异常用例数：'+str(err_no)+'，执行耗时：'+str(time_cost)+'秒')

    #测试完毕发送邮件
    if not case_err:
        #如果用例检测通过，则会执行测试，此时才会产生case_html_output
        fhtml=getcwd()+r'/result/gtestreport'+str(int(time()))+'.html'
        reporter=htmlreporter(fhtml,case_html_output)
        reporter.make_report()
        logger.sendlog(fhtml)
    else:
        logger.sendlog()


if __name__=="__main__":
    main()


