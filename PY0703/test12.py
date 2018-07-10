# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
class A():
    '''
    >>> a = A()
    >>> a.out()
    1
    '''

    def out(self):
        print(1)

import doctest
doctest.testmod()
