#coding:utf-8
#请求头定义
dl_header=\
    {'DEVICESIZE': '640*960',
     'DLTOKEN': '15d08261f6bb53e4ab4b29793e21dca4',
     'SYSTEMVERSION': '7.1.2',
     'DLFINGER': '9ae396cb490ff26e78c3439431d9699a',
     'CHANNELID': 'App Store',
     'IDFV': '8B5E298B-8744-452B-893F-69527BE57C4E',
     'Connection': 'close',
     'Accept-Encoding': 'gzip',
     'User-Agent': '达令全球好货 5.7.5 rv:5.7.5.0 (iPhone; iPhone OS 7.1.2; en_US)',
     'APPVERSION': '5.7.5',
     'MAC': '02:00:00:00:00:00',
     'UID': '',
     'APPNAME': 'com.daling.daling',
     'IDFA': '083A973F-FC5C-4B8E-8A71-CC7D2E407E5B',
     'DEVICEMODE': 'iPhone',
     'CLIENTID': '587523b46d9f0d034017c09fde97a703343fc25e',
     'PLATFORM': 'iphone',
     'Connection': 'close',
     'ACCESSTOKEN': '',
     'Pragma': 'no-cache'}


#case_list定义
case=[{'case_name':'用例1','case_content':'测试测试1','url':'http://m.ymall.com/api/goods/detail?goods_id=166520','method':'GET','header':dl_header,'expect_json':{'data':{'goods_id':166520,'status':12}}},
      {'case_name':'用例2','case_content':'测试测试2','url':'http://m.ymall.com/api/goods/detail?goods_id=166521','method':'GET','header':dl_header,'expect_json':{'data':{'goods_id':'166520','status':12}}},
      {'case_name':'用例3','case_content':'测试测试3','url':'http://m.ymall.com/api/goods/detail?goods_id=167738','method':'GET','header':dl_header,'expect_json':{'data':{'goods_id':167738,'status':'12'}}},
      {'case_name':'用例4','case_content':'测试测试4','url':'http://m.ymall.com/api/goods/detail?goods_id=167756','method':'GET','header':dl_header,'expect_json':{'data':{'goods_id':167755,'status':12}}},
      {'case_name':'用例5','case_content':'测试测试5','url':'m.ymall.com/api/goods/detail?goods_id=167756','method':'GET','header':dl_header,'expect_json':{'data':{'goods_id':167755,'status':12}}}
      ]
