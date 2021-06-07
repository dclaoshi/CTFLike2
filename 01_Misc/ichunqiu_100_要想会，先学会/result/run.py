#!/usr/bin/env python2
# -*- coding: utf-8 -*-
a=[144,144,150,139,145,165,120,139,91,160,93,167,70]
for j in range(-50,50):
  flag=''
  for i in a:
    flag+=chr(i+j)
  print flag