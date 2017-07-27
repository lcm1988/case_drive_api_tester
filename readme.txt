一，python环境所需工具类：
    httplib2和xmltodict 需要额外安装，安装方法自己百度
    json、urllib均为python自带工具类

二，case.py文件主要为接口输入数据的list，主程序会加载这个list遍历请求接口，故测试时主要维护这个文件就可以

三，run.py为主程序，除对测试流程有额外需求外一般不用修改，预期数据和实际返回数据可以转成dict然后用datacompare方法进行对比（这个自己加）

四，有事可以及时找我