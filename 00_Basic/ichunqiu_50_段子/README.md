# 段子

## 题目描述
---
程序猿圈子里有个非常著名的段子：

手持两把锟斤拷，口中疾呼烫烫烫。

请提交其中"锟斤拷"的十六进制编码。(大写)

## 题目来源
---
ichunqiu ISC2016训练赛——phrackCTF

## 主要知识点
---


## 题目分值
---
50

## 部署方式
---
无

## 解题思路
---

锟斤拷的来历 GBK与UTF-8   

Unicode和老编码体系的转化进程中，一定有一些字，用Unicode是没法表示的，Unicode官方用了一个占位符来表示这些文字，这就是：U+FFFD REPLACEMENT CHARACTER。

那么U+FFFD的UTF-8编码出来，恰恰是 "\xef\xbf\xbd"。假如这个"\xef\xbf\xbd"，反复屡次，例如 "\xef\xbf\xbd\xef\xbf\xbd"，然后放到GBK/CP936/GB2312/GB18030的环境中显示的话，一个汉字2个字节，最终的后果就是：锟斤拷""锟(0xEFBF)，斤（0xBDEF），拷（0xBFBD）

烫烫烫的来历 vc++：

在windows平台下，ms的编译器（也就是vc带的那个）在 Debug 形式下，会把未初始化的栈内存全部填成 0xcc，用字符串来看就是"烫烫烫烫烫烫烫"，也就是说呈现了烫烫烫，赶忙反省初始化吧

屯屯屯的来历 VC：

同上，未初始化的堆内存全部填成0xcd，字符串看就是"屯屯屯屯屯屯屯屯"。

锘的来历 VC HTML：

微软在 UTF-8 文件头部加上了 EF BB BF BOM 标志。在不支持 BOM 的环境下对其停止 UTF-8 解码失掉"锘"字。

所以答案为锟(0xEFBF)，斤（0xBDEF），拷（0xBFBD）

PCTF{EFBFBDEFBFBD}