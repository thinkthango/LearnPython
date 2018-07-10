# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
import chardet
data='天王盖地虎,小鸡炖蘑菇'.encode('utf-8')
print(chardet.detect(data))
# {'language': 'Chinese', 'confidence': 0.7407407407407407, 'encoding': 'GB2312'}
data='天王盖地虎,'.encode('gbk')
print(chardet.detect(data))
# {'language': None, 'confidence': 0.0, 'encoding': None}