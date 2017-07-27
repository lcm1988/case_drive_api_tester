#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from conf.config import RECIEVER_LIST,SMTP_SERVER,EMAIL_NAME,EMAIL_PWD

class testlogger():
    def __init__(self,fpath):
        self.fpath=fpath
        #收件人
        self.receiver = RECIEVER_LIST
        #发件服务器
        self.smtpserver = SMTP_SERVER
        #邮箱口令
        self.name = EMAIL_NAME
        self.pwd = EMAIL_PWD

    #追加写入log
    def writelog(self,content):
        f=open(self.fpath,'a')
        f.writelines(content)
        f.writelines('\n')
        f.close()

    #发送邮件
    def sendlog(self,fhtml=''):
        #创建一个带附件的实例
        msg = MIMEMultipart()

        #构造文本
        att1 = MIMEText('您好，测试已执行完毕，结果日志见附件','plain')
        msg.attach(att1)

        #构造log附件
        att2 = MIMEText(open(self.fpath, 'rb').read(), 'base64','utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="TEST_LOG.txt"'
        msg.attach(att2)

        if fhtml:
            #构造log附件
            att3 = MIMEText(open(fhtml, 'rb').read(), 'base64','utf-8')
            att3["Content-Type"] = 'application/octet-stream'
            att3["Content-Disposition"] = 'attachment; filename="TEST_REPORT.HTML"'
            msg.attach(att3)

        #构造剩余数据
        msg['Subject'] = u'TEST LOG'
        msg['From'] = self.name
        msg['To'] = ";".join(self.receiver)

        #登录发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(self.smtpserver,25)
        smtp.login(self.name, self.pwd)
        smtp.sendmail(self.name, self.receiver, msg.as_string())
        smtp.quit()

if __name__=="__main__":
    l=testlogger(r'f:\newlog.txt')
    for i in range(0,10):
        l.writelog(str(i)+'测试结果\n')
    l.sendlog()