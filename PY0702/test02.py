# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
import functools

def log(text):
    def decorator(fnc):
        @functools.wraps(fnc)
        def wrapper(*args,**kw):
            print('in fnction:%s' %(fnc.__name__) )
            return fnc(*args,**kw)
        return wrapper
    if callable(text):
        return decorator(text)
    else:
        print('text:%s' %text)
        return decorator

@log
def f1():
    print('f1')

@log('execute')
def f2():
    print('f2')

f1()
f2()