# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
class Animal(object):
	"""docstring for ClassName"""
	__slots__ = ('name','age')

class Dog(Animal):
	pass


ani = Animal()
ani.name='myname'
ani.ss='ss'
dog = Dog()
dog.ss='ss'

