# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
def person(*,name, age, city, job):
    print(name, age, city, job)

# person(name='Jack',age=24,city='Beijing',job='Engineer')

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


import PY0627.test03
print(say())
