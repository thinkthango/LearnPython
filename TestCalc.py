# -*- coding:utf-8 -*-
#__author__ :kusy
#__content__:文件说明
#__date__:2018/7/19 13:51

xSum = 0
for x in range(101):
    xSum = xSum + x
print(xSum)

xSum=0
x = 1
while x <101:
    xSum = xSum + x
    x+=1

print(xSum)


def my_sum(i):
    return my_sum(i-1) + i if i!=0 else 0

print(my_sum(100))

