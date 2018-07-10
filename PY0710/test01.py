# -*- coding:utf-8 -*-
#__author__ :kusy
#__content__:文件说明
#__date__:2018/7/10 13:17


def Gne():
    i = 5
    # print('开服第%d天，在线人数：%d' %((6-i),i))
    while True:
        if i == 1 :
            break
        yield i
        i -= 1
        print('开服第%d天，在线人数：%d' %((5-i),i))
    # print('i after : %d' %i)

g = Gne()
while True:
    try:
        g.__next__()
    except StopIteration:
        break

