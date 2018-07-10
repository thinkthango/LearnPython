# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
from io import StringIO

f = StringIO()
f.write('Hello ')
f.write('World')
f.close()
# print(f.getvalue())

# print(f.tell())
# f.seek(0)
print(f.read())

# fr = StringIO('aabbcc\n dd')
# print(fr.readline().strip())
# print(fr.readline().strip())
#
# print('  ss   bb \n'.strip(' '))
# print('  ss   bb '.strip())

