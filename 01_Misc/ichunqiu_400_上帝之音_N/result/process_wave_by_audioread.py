
#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2021年6月13日21:07:10
@description : 处理wave
@Update date :  
"""  

import audioread

with audioread.audio_open("godwave.wav") as f:
    print(f.channels, f.samplerate, f.duration)
    for buf in f:
        print(buf)