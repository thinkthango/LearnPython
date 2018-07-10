# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Type Error')

if __name__ == '__main__':
    my_abs('s')

# def my_bas(x):
# 	if not isinstance(x,(int,float)):
# 		raise TypeError('bad operand type')
# 	else:
# 		pass
#
# if __name__ == '__main__':
#     my_bas('a')