# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    # def __getattr__(self, path):
    #     return Chain('%s/%s' % (self._path, path))
    #
    # def __str__(self):
    #     return self._path
    #
    # __repr__ = __str__

    def __call__(self, *args, **kwargs):
        print("call myself path:%s" %self._path)


# print(Chain().status.user.timeline.list)
c = Chain()
print(c())
