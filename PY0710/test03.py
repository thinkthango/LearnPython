# -*- coding:utf-8 -*-
#__author__ :kusy
#__content__:文件说明
#__date__:2018/7/10 16:27
def g1():
     yield  range(5)
def g2():
     print('s')
     yield  from range(5)
     print('e')


it1 = g1()
it2 = g2()
for x in it1:
    print(x)

for x in it2:
    print(x)

