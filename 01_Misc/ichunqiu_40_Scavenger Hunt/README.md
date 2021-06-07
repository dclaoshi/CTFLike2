# Scavenger Hunt

## 题目描述
---
```
There is a flag hidden somewhere on our website, do you think you can find it? Good luck! 
```

## 题目来源
---
IceCTF

## 主要知识点
---


## 题目分值
---
40

## 部署方式
---


## 解题思路
---

flag 在 icectf-2016 的网站中，但是已经无法访问了

参考[https://github.com/ctfs/write-ups-2016/tree/master/icectf-2016/misc/scavenger-hunt-50](https://github.com/ctfs/write-ups-2016/tree/master/icectf-2016/misc/scavenger-hunt-50)

To search for the flag manually, press Ctrl+U on each page (it's on the sponsors page) and Ctr+F search the source code for the string `IceCTF{` until you find the flag, or for a quicker method, use the Linux bash command `wget -r *.icec.tf.* | grep "IceCTF{"` to download the website and filter the results using `grep` to find this on the sponsors page: `<img class="activator" src="/static/images/logos/syndis.png" alt="IceCTF{Y0u_c4n7_533_ME_iM_h1Din9}">` which contains the flag in the alternate attribute.

## 参考
---
* [RawSec](https://rawsec.ml/en/IceCTF-50-Scavenger-Hunt-Misc/)
* http://0xbugsbunny.blogspot.com/2016/08/icectfwriteupstage1stage2.html
* https://capturetheflags.blogspot.in/2016/08/icectf-2016-scavenger-hunt-writeup.html
* https://youtu.be/CyvjUXW5quE
* https://github.com/Idomin/CTF-Writeups/blob/master/IceCTF/ScavengerHunt-Misc-50
* http://5k33tz.com/icectf-scavenger-hunt/
* https://github.com/Beers4Flags/writeups/tree/master/IceCTF2016/misc/scavenger_hunt