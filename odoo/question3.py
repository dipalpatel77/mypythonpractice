'''Write a program which accepts a sequence of comma-separated numbers from 
console and generate a list and a tuple which contains every number.'''
d = input()
x = []
for c in d:
	if c != ',':
		x.append(c)
# for i in x:
# 	if isinstance(i,str):
# 		print int(i)
print x
print tuple(x)