# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

print(__name__)
if __name__=='__main__':
    test()