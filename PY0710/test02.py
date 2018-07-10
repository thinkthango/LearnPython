# -*- coding:utf-8 -*-
#__author__ :kusy
#__content__:文件说明
#__date__:2018/7/10 15:36
import random

# def mygen(alist):
#     while len(alist) > 0:
#         c = random.random(0, len(alist)-1)
#         yield alist.pop(c)
# a = ["aa","bb","cc"]
# c=mygen(a)
# print(c)

def gen():
    value=0
    while True:
        receive=yield value
        if receive=='e':
            break
        value = 'got: %s' % receive

g=gen()
print(g.send(None))
print(g.send('hello'))
print(g.send(123456))
print(g.send('e'))
