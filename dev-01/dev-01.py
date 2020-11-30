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
import sys
import os
import subprocess
# r = subprocess.call('cmd /c dir')
# # r = os.system('dir')
# # print("没问题",r)
# # r = os.popen('dir')
# print("输出结果"+r.decode('GBK'))
# pipe = subprocess.Popen('cmd /c dir',stdout=subprocess.PIPE)
# r = pipe.stdout.read()
# print(r)
# print(r.decode('gbk'))

# args = sys.argv

# def add(a,b):
#     return a+b
# if __name__ == "__main__":
#     if len(args) < 3:
#         print("arg1,arg2")
#     else:
#         r = add(args[1],args[2])
#         print(r)
# r = os.environ
# print(r)
# print(r["path"],["classpath"])

import threading,time
# def helloworld():
#     time.sleep(5)
#     print("hello %d world" % id)
#
#
# for i in range(5):
#     t = threading.Thread(target=helloworld,args=(i,))
#     t.start()
# print("main thread")
# def test1():
#     time.sleep(10)
#     print("task done " "\n")
# def test2():
#     time.sleep(10)
#     print("task done")
# lock = threading.Lock()
# def count(i):
#     time.sleep(1)
#     with lock:
#         print(i)
# #with  上下文管理器，ender  exit
# threads = []
# for i in range(1000):
#     thread = threading.Thread(target=count,args=(i,))
#     threads.append(thread)
#
# for thread in threads:
#     thread.start()
# from urllib import request
# import threading,queue
# url = "https://www.baidu.com"
# q = queue.Queue()
# for i in range(10):
#     q.put(i)
# def get_lvgw():
#     while True:
#         try:
#             q.get(block = False)
#             r = request.urlopen(url)
#             print(r.code,"\n","成功")
#         except queue.Empty:
#             break
# ts = []
# print(ts)
# for i in range(10):
#     t = threading.Thread(target=get_lvgw())
#     ts.append(t)
#     t.start()
# if __name__ == "__main__":
    # start = time.time()
    # t = threading.Thread(target=test1)
    # t2 = threading.Thread(target=test2)
    # t.start()
    # t2.start()
    # t.join()
    # t2.join()
    # end = time.time()
    # print(end-start)

def digui(n):
    if n == 1:
        return 1
    else:
        return n*digui(n-1)

if __name__ == "__main__":
    print(digui(10))