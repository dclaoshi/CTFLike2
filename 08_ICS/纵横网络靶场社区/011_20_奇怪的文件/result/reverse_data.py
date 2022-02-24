#!/usr/bin/env python3
# 读文件
with open("KeyVisual_unkonw_data.bin", "rb") as f:
    data = f.read()

# 写文件
with open("new_data.zip", "wb") as f:
    f.write(data[::-1])