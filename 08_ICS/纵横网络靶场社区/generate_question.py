# -*- coding:utf8 -*-
import json
import os
"""
通过结果数据生成纵横网络靶场目录

https://game.fengtaisec.com/competition/frontend/questions/?page=1&pageSize=30&question_tags=1
"""

datas = open("question_datas.json", encoding = "utf-8").read()

datajson = json.loads(datas, strict=False)
for data in datajson["data"]:
    '''
    {'id': 173, 'name': '隐藏的工艺', 'deal_num': 19, 'explain': '工控安全工程师把工艺流程分享在论坛中，并留下关键敏感信息，你能找到相关线索吗？flag格式为:flag{}。', 'question_tags': 1, 'get_question_tags_display': '离线赛题', 'created_local_time': '2021-07-02 10:38:07', 'author_name': '管理员', 'fraction': 10, 'author': 1, 'level': 1, 'writeup_num': 2, 'challenge_num': 20, 'question_abilitys_info': [{'id': 1, 'name': '溯源及归因'}, {'id': 4, 'name': '工业应用安全'}, {'id': 5, 'name': '工业网络渗透'}], 'challenge_status': None}
    '''
    # print(data)
    mkpath = "{:0>3d}_{}_{}".format(data["id"], data["fraction"], data["name"])
    if os.path.exists(mkpath):
        print(mkpath + "已存在")
        continue
    print(mkpath)
    os.mkdir(mkpath)

    submkdpaths = [mkpath + "/images",
                    mkpath + "/reference",
                    mkpath + "/resources",
                    mkpath + "/result",]

    for submkpath in submkdpaths:
        os.mkdir(submkpath)

    reademetxt = """# %s

## 题目描述
---
> %s

## 题目来源
---
纵横网络靶场社区 https://game.fengtaisec.com/

## 主要知识点
---


## 附件
---


## 题目分值
---
%d

## 部署方式
---


## 解题思路
---


## Flag
---


## 参考
---
"""% (data["name"], data["explain"], data["fraction"])
    
    open(mkpath + "/README.MD", "w", encoding = "utf-8").write(reademetxt)