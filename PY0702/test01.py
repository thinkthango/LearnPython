# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明

import time,functools
def A(fnc):
    print('A')
    def wrapper(*args,**kw):
        return fnc(*args,**kw)
    return wrapper

def B(fnc):
    print('B')
    return fnc

@B
def say(s):
    print(s)

# say('sss')



def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        t1 = time.time()
        f = fn(*args,**kw)
        t2 = time.time()
        print('%s executed in %f ms' % (fn.__name__, float(t2)-float(t1)))
        return f
    return wrapper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')