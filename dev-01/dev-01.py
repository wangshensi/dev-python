#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-25 17:08
# @Author  : Curry.S

# def out_f(arg):
#     print("out_f"+arg)
#     def decorator(func):
#         def inner():
#             func()
#         return inner
#     return decorator
# @out_f("123")
# def func():
#     print("hello world")
#
# func()

import os
import subprocess
# r = subprocess.call('cmd /c dir')
# # r = os.system('dir')
# # print("没问题",r)
# # r = os.popen('dir')
# print("输出结果"+r.decode('GBK'))
pipe = subprocess.Popen('cmd /c dir',stdout=subprocess.PIPE)
r = pipe.stdout.read()
print(r)
print(r.decode('gbk'))
