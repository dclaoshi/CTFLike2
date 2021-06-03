# coding:utf8
import requests
import base64
url = "http://ctf5.shiyanbar.com/web/10/10.php" # 目标URL

response = requests.post(url,data={"key":"1"}) # 打开链接
print response
head = response.headers # 获取响应头
flag = base64.b64decode(head['flag']).split(':')[1] # 获取相应头中的Flag
print flag # 打印Flag
postData = {'key': flag} # 构造Post请求体
result = requests.post(url=url, data=postData) # 利用Post方式发送请求 
# (注意要在同一个Session中 , 有的时候还需要设置Cookies , 但是此题不需要)
print result.text # 打印响应内容
