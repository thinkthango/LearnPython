# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
def count():
    fs = []
    for i in range(1, 4):
        def f():
             print(i)
             return i*i
        fs.append(f)
    return fs

# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())
print(count()[0]())
