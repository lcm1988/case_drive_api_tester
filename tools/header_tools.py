#coding:utf-8
class headertools():
    def __init__(self):
        pass
    #将dict形式的header存放在缓存文件并返回文件路径，用以解决频繁调用登录方法时触发鉴权限制问题
    def saveHeader(self,header,fpath=r'./cache'):
        try:
            fp=open(fpath,'w')
            for key,value in header.items():
                line= key+':'+str(value)+'\n'
                fp.write(line)
            fp.close()
        except Exception as e:
            print e

    #文件读取rawheader自动滤掉行末换行符、空行并转换成dict格式的header
    def loadHeader(self,fpath=r'./cache'):
        #import platform
        #print platform.system()
        #windows输出：Windows  MAC输出：Darwin  linux系统输出待定
        f=open(fpath)
        headers={}
        for line in f:
            if line[0] != '#' and line[0] != '\n':
                key=line.split(':')[0].strip()
                #去掉行末换行符：具体视编辑工具而定，该脚本只考虑\n，可以做其他环境兼容，windows的默认换行是\r\n，unix的是\n，mac的是\r，
                if line[-1]=='\n':
                    value=line.split(':')[1][0:-1].strip()
                else:
                    value=line.split(':')[1].strip()
                headers[key]=value
        return headers



