#coding:utf-8
import xmltodict as xd
import json

class xmltransfer():
    def __init__(self):
        pass

    #定义xml转换字典方法
    def xml_to_dict(self,xmlstr):
        try:
            trans_str=xd.parse(xmlstr)
            json_data=json.dumps(trans_str)
            json_data=json.loads(json_data)
            return json_data
        except Exception,e:
            print Exception,e

    #定义字典转换xml方法
    def dict_to_xml(self,dict_data={}):
        try:
            if len(dict_data.keys())==1:
                return xd.unparse(dict_data)
            else:
                raise ValueError,u'wrong frame of dict'
        except Exception,e:
            print Exception,e


if __name__=="__main__":
    test_str="<student><info><mail>xxx@xxx.com</mail><name>name</name><sex>male</sex></info><course><score>90</score><name>math</name></course><course><score>88</score><name>english</name></course><stid>10213</stid></student>"
    a= xmltransfer().xml_to_dict(test_str)
    print a
    b=xmltransfer().dict_to_xml(a)
    print b