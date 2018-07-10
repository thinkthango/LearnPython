# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明

# try:
#     f = open('test.txt','r',encoding='utf-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()

with open('test.txt','r',encoding='utf-8') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    # for line in f.readlines():
    #     print(line.strip())
    # while True:
    #     try:
    #         print(f.read(1))
    #     except EOFError:
    #         break

# with open('test.txt','w',encoding='utf-8') as f:
#     f.write('枫桥夜泊（张继）\n')
#     f.write('月落乌啼霜满天，江枫渔火对愁眠；\n')
#     f.write('姑苏城外寒山寺，夜半钟声到客船。\n')



