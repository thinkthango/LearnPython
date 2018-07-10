# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda :25


s = Student()
print(s.score)
print(s.age)
print(s.none)
