__author__ = 'DIPAL'
a,b=1,1
c=[]
print(a)
print(b)
n=input()
for i in range(n):
    a,b=b,a+b
    print(a)
    c.append(a)


print(c)