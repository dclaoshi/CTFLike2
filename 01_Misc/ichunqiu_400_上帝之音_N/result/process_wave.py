
#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
@Author : darkN0te
@Create date : 2021年6月13日21:07:10
@description : 处理wave
@Update date :  


wave 常用函数

打开wav文件：wav = wave.open("文件名","rb")
读取全部帧：wav.readframes()
获取帧数：wav.getnframes()
获取声道数：wav.getnchannels()
获取帧速率：wav.getframerate()
获取比特宽度(即每一帧的字节数)：wav.getsampwidth()

参考 https://www.bbsmax.com/A/mo5kKEqM5w/
"""  


import wave
import numpy as np

# 打开wav文档
w = wave.open("godwave.wav")

# 读取格式信息
# (nchannels, sampwidth,framerate, nframes, comptype, compname)
params = w.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
# Duration 也就是音频时长 = 采样点数/采样率 
Duration = wav_time = nframes / float(framerate)  # 单位为s
print("音频头参数：", params)
print("通道数(Channels)：", nchannels)
print("采样率(SampleRate)：", sampwidth)
print("比特(Precision)：", framerate)
print("采样点数(frames)：", nframes)
print("帧数或者时间(Duration)：", Duration)


# 读取波形数据
str_data  = w.readframes(nframes)
# 文件使用完毕,关闭文件
w.close()
 
# 将波形数据装换成数组
wave_data = np.frombuffer(str_data, dtype=np.short)

threshold_positive = 0
threshold_negative = -0
result = []

for i in range(64):
    print(wave_data[i],end=',')
    if wave_data[i] > threshold_positive:
        result.append('1') 
    elif wave_data[i] < threshold_negative:
        result.append('0')
    else:
        pass
print(len(result))
data = "".join(result)
print(data)
ans = ''
count = 0
res = 0
while data != '':
    pac = data[:2]
    if pac != '':
        if pac[0] == '0' and pac[1] == '1':
            res = (res<<1)|0
            count += 1
        if pac[0] == '1' and pac[1] == '0':
            res = (res<<1)|1
            count += 1
        if count == 8:
            ans += chr(res)
            count = 0
            res = 0
    else:
        break
    data = data[2:]
print(ans)

with open('out.png', 'wb') as f2:
    f2.write(ans.encode())