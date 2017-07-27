#coding:utf-8

#数据对比，根据数据结构递归对比
def datacompare(expect_data,real_data,path='/root',err_list=[]):
    if isinstance(expect_data,(list,tuple)):
        for index,value in enumerate(expect_data):
            try:
                if not isinstance(value,(list,dict,tuple)):
                    #转换为unicode编码对比
                    if isinstance(value,str):
                        value=value.decode('utf-8')
                    if value==real_data[index]:
                        #对比一致
                        continue
                    else:
                        err_list.append(path+'/'+str(index)+':'+'预期值：'+str(value)+str(type(value))+'实际值：'+str(real_data[index])+str(type(real_data[index]))+'对比不一致')
                else:
                    err_list=datacompare(value,real_data[index],path+'/'+str(index),err_list)
            except Exception, e:
                print Exception,e
    elif isinstance(expect_data,dict):
        for key,value in expect_data.items():
            try:
                if not isinstance(value,(list,dict,tuple)):
                    #转换为unicode编码对比
                    if isinstance(value,str):
                        value=value.decode('utf-8')
                    if value==real_data[key]:
                        #对比一致
                        continue
                    else:
                        err_list.append(path+'/'+str(key)+':'+'预期值：'+str(value)+str(type(value))+'实际值：'+str(real_data[key])+str(type(real_data[key]))+'对比不一致')
                else:
                    err_list=datacompare(value,real_data[key],str(path)+'/'+str(key),err_list)
            except Exception,e:
                print Exception,e
    else:
        if not expect_data==real_data:
            err_list.append(path+':'+str(expect_data)+str(type(expect_data))+str(real_data)+str(type(real_data))+'对比不一致')
    return err_list

if __name__=="__main__":
    a=[{"name":['a','b',1,1],"grade":2,"score":{'math':[{"name":['a','b',1,1]},{"name":['a','b',1,1]},'3'],'eng':100}},{"name":['a','b',1,1],"grade":2,"score":{'math':[{"name":['a','b',1,1]},{"name":['a','b',1,1]},'3'],'eng':100}}]
    b=[{"name":['a','b',1,2],"grade":1,"score":{'math':[{"name":['a','b',1,2]},{"name":['a','b',1,1]},3],'eng':100}},{"name":['a','b',1,2],"grade":1,"score":{'math':[{"name":['a','b',1,2]},{"name":['a','b',1,1]},3],'eng':100}}]
    c=[[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
    d=[[1,2,3],[1,'2',3],[1,2,3],[1,2,3]]
    for index,val in enumerate(c):
        l=datacompare(val,d[index],'/',[])
        for i in l:
            print i
    #from dapiauto import UserCenterClass