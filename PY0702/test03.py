# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明

import functools
int2 = functools.partial(int,base=2)
print(int2('1000000'))
print(functools.partial(max,10)(1,3,2,11))
