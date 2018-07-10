# -*- coding:utf-8 -*-
#__author__ :suneee
#__content__:说明
def trim(s):
	newS=""
	for i in range(len(s)):
		if s[i:i+1] != " ":
			newS = newS + s[i:i+1]
	return newS

def trim2(s):
    if (s[:1] == ' '):
        return trim(s[1:])
    elif (s[-1:] == ' '):
        return trim(s[:-1])
    else:
        return s

def trim3(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s
print(trim3("   abc d      "))

print(enumerate(['A', 'B', 'C']).next)