题目描述：
```
You have found a passwd file containing salted passwords. An unprotected configuration file has revealed a salt of 5948. The hashed password for the 'admin' user appears to be 81bdf501ef206ae7d3b92070196f7e98, try to brute force this password.

您找到了一个有盐的密码表。已知密码的明文结尾为5948，密码表中哈希值为81bdf501ef206ae7d3b92070196f7e98，尝试暴力破解此密码。
```

原题干为英文，但是感觉和题目本身的意思不一样，写了一段和原题目意思一致的中文。题目的意思就是一个简单的爆破md5。难点是不知道到底这个明文到底有多少位，都包含什么字符。

这里直接使用在cmd5上查到的结果`sniper5948`。