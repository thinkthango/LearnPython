# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
import json

d= dict(key1='value1',key2='value2',key3='value3')
jd = json.dumps(d)

print(json.loads(jd))
