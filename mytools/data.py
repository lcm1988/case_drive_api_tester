#coding:utf-8
import random
import sys
sys.path.append("f:\\")
import t
class myException(Exception):
      def __init__(self, x, y):
            Exception.__init__ (self, x, y)
            self.code = x
            self.msg = y

def datatable(filepath):
    t=[]
    fileobj=open(filepath,'r')
    if isinstance(fileobj,file):
        for i in fileobj:
            t.append([k.strip() for k in i.strip().split(',')])
        return t
    else:
        raise myException(1001,'invalid file')

def getrand(x):
    res= int(random.random()*100)
    if x>100:
        raise ValueError,'Please enter an integer less than 100'
    if int(res/x)<1:
        return True
    else:
        return False

f=open(r'f:\goods.csv')
print type(f)
print 'abc    \r\n'.strip(),123
print
a=b=0
for i in range(10000):
    if getrand(100):
        a=a+1
    else:
        b=b+1
print a,b

