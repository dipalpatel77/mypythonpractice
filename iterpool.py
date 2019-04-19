# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = list()
b = list()
x = raw_input("enter no").split()
for i in(x):
	a.append(int(i))
print a
print "type of raw in	put after type cast",	type(x)
y = raw_input("enter no").split()
for i in(y):
	b.append(int(i))
print a,b    
c = list(product(a,b))
print c

print ' '.join(map(str,c))
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = list()
b = list()
x = raw_input().split()
y = raw_input().split()
for i in(x):
	a.append(int(i))
for i in(y):
	b.append(int(i))
c = list(product(a,b))
print ' '.join(map(str, c))
#print str(c)[1:-1]
'''