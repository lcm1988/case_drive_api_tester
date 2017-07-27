#coding:utf-8
from conf.config import REPORT_TITTLE,REPORT_CONTENT

#该文件负责将log转换成html格式的报告
class htmlreporter():
    def __init__(self,fpath,column_values=[],report_title=REPORT_TITTLE,report_content=REPORT_CONTENT):
        #文件路径
        self.fpath=fpath

        #网页title
        if isinstance(report_title,(str,basestring,unicode)):
            self.title=report_title
        else:
            self.title=REPORT_TITTLE

        #报告标题
        if isinstance(report_content,(str,basestring,unicode)):
            self.content=report_content.replace('<','&lt;').replace('>','&gt;')
        else:
            self.content=REPORT_CONTENT

        #case执行结果
        if isinstance(column_values,list):
            self.column_values=column_values
        else:
            self.column_values=[]

        self.table=self.make_table()
        pass

    #自动生成html网页的table模块
    def make_table(self):
        table_begin=\
            '''
            <table class="table">
            <tr><th>用例名称</th><th width="200">用例说明</th><th>执行结果</th><th width="600">详细信息</th></tr>
            '''
        table_end=\
            '''
            </table>
            '''
        tr_list=[]
        pass_no=fail_no=err_no=0
        for idx,val in enumerate(self.column_values):
            #协程处理时结果顺序不确定，不再设置默认用例名称
            #case_name=val[0].replace('<','&lt;').replace('>','&gt;') if val[0] else '用例'+str(idx+1)
            case_name=val[0].replace('<','&lt;').replace('>','&gt;') if val[0] else ''
            case_content=val[1].replace('<','&lt;').replace('>','&gt;') if val[1] else '暂无信息'
            if val[2]==0:
                case_res='测试失败'
                fail_no+=1
            elif val[2]==1:
                case_res='测试通过'
                pass_no+=1
            else:
                case_res='执行异常'
                err_no+=1
            case_msg=val[3] if val[3] else '暂无信息'
            tr_str='''<tr><td>'''+case_name+'''</td><td>'''+case_content+'''</td><td>'''+case_res+'''</td><td><input type="button" value="查看" id="b%d" onClick="showElement('b%d','t%d')"/><p id="t%d" style="line-height:20px;display:none">'''%(idx,idx,idx,idx)+case_msg+'''</p></td></tr>'''
            tr_list.append(tr_str)
        table_val='\r\n'.join(tr_list)
        table_count='''<tr><td colspan="4"></p>执行结果：用例总数-%d; 通过-%d ; 失败-%d; 异常-%d;</p></td></tr>'''%(len(self.column_values),pass_no,fail_no,err_no)
        return table_begin+table_val+table_count+table_end

    #生成网页源码
    def make_report(self):
        f=open(self.fpath,'w')
        htmlstr=\
            '''
            <!DOCTYPE html>
            <html>
            <head>
            	<meta charset="utf-8">
                <title>'''+self.title+'''</title>
            	<style type="text/css">
            		body,table{
            			font-size:12px;
            		}
            		table{
            			table-layout:fixed;
            			empty-cells:show;
            			border-collapse: collapse;
            			margin:0 auto;
            		}
            		td{
            			height:30px;
            		}
            		.table{
            			border:1px solid #cad9ea;
            			color:#666;
            		}
            		.table th {
            			background-repeat:repeat-x;
            			height:30px;
            		}
            		.table td,.table th{
            			border:1px solid #cad9ea;
            			padding:0 1em 0;
            		}
            		.table tr.alter{
            			background-color:#f5fafe;
            		}
            	</style>
            	<script type="text/javascript">
            	//控制控件展开、收起
            	function showElement(id1,id2){
            		if (document.getElementById(id1).value=="查看"){
            			document.getElementById(id2).style.display="block";
            			document.getElementById(id1).value="收起";
            			}
            		else {
            			document.getElementById(id2).style.display="none";
            			document.getElementById(id1).value="查看";
            			}
            		}
            	</script>
            </head>
            <body>
            <h1 align="center" style="color:#cad9ea;font-size:16px;">===================================================</h1>
            <h1 align="center" style="color:#666;font-size:16px;">'''+self.content+'''</h1>
            <h1 align="center" style="color:#cad9ea;font-size:16px;">===================================================</h1>
                <div>
            '''+self.table+'''
                </div>
            </body>
            </html>
            '''
        f.write(htmlstr)
        f.close()

if __name__=="__main__":
    case_res=[['测试用例1','姓名输入中文',1,'测试通过'],
              ['测试用例2','姓名输入英文',0,'''节点:/data/goods_id:预期值：167755&lt;type 'int'&gt;实际值：167756&lt;type 'unicode'&gt;对比不一致<br>节点:/data/goods_id:预期值：167755&lt;type 'int'&gt;实际值：167756&lt;type 'unicode'&gt;对比不一致<br>节点:/data/goods_id:预期值：167755&lt;type 'int'&gt;实际值：167756&lt;type 'unicode'&gt;对比不一致'''],
              ['测试用例3','姓名输入数字',0,'测试通过'],
              ['测试用例4','姓名输入中文+英文',1,'测试通过']]
    h=htmlreporter(r"f:\reporter.html",case_res)
    h.make_report()
    #a='''He is %d years old'''%(25)
    #print a