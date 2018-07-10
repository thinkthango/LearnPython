# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A):
    def bar(self):
        print('C1-bar')

class C2(B):
    def bar(self):
        print('C2-bar')

class D(C2,C1):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo()
    d.bar()