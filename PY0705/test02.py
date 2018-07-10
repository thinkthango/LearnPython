# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
import base64

def safe_base64_decode(s):
    s = s + (4-len(s)%4) * b'=' if len(s)%4 else s
    return base64.b64decode(s)


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')