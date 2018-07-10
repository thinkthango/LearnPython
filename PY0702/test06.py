# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
class Student(object):
    def __init__(self,name,score):
        self.name=name
        # self.score=score
        self.__score=score
    def out(self):
        print(self.name,self.__score)


class StudentLittle(Student):
    pass

s1 = Student('sky',66)
s1.__score=1
print( s1._Student__score)

s2 = Student('sky',66)
s2.ss='sss'
print(s1.out())

s3 = StudentLittle('name',100)
s3.out()

def duck(stu):
    stu.out()

duck(s1)