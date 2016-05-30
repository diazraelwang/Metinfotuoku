class Outputer(object):
    
    
    def output_to_html(self,datas,columns):
        if datas is None:
            return
        fout = open('d:/metinfotable.html','w')
        
        # ascii
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        for data_key in datas:
            a_datas = datas[data_key]
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data_key)
            for dic_key in a_datas :
                fout.write("<td>%s</td>" % a_datas[dic_key].encode("utf-8"))
            fout.write("</tr>")
    
        fout.write("</html>")
        fout.write("</body>")
        fout.write("</table>")
    



