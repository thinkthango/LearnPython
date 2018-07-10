# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明


from collections import namedtuple,deque,defaultdict
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x,p.y)


q = deque(['a','b','c'])
q.pop()
q.appendleft('z')
print(q)

dd = defaultdict(lambda :'N/A')
dd['key1'] = 'value1'
print(dd['key1'])
print(dd['key2'])


