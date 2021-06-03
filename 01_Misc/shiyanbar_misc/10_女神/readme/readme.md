# 女神

## 题目描述
```
猫流大大发现一个女神，你能告诉我女神的名字么（名字即是flag）
解题链接： nvshen.zip
```

## 解题思路
看到密文后，一段代码解密。

```python
#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2018-07-11
@description : Base64 to file
@Update date :   
@User : python run.py a.txt
"""  
import sys

input = sys.argv[1]
f = open(input,"rb")
content = f.read().decode("base64")
f.close()
f = open(input + "_decode","w")
f.write(content)
f.close()
```

发现是个妹子图片。但是我认识她是谁啊，只能google了。

![](2018-07-11-13-52-17.png)

原来是Aisin Gioro，还是不认识。