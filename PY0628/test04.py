# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
def createCounter():
        j = 0
        def counter():
            nonlocal j
            j=j+1
            return j
        return counter

counterA = createCounter()
counterA()
counterA()
counterA()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')