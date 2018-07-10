# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a,self.b = 0,1

	def __iter__(self):
		return self

	def __next__(self):
		self.a,self.b = self.b,self.a + self.b
		if self.a > 100:
			raise StopIteration()
		return self.a

	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a

for n in Fib():
	print(n)

print(Fib()[0])
