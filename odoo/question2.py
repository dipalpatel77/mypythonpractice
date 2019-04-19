# a = []
# for i in range(1,input()+1):
# 	a[i:1]=[i,i*i]
# print a
# a = []
# for i in range(1,input()+1):
# 	a.append(i)
# 	a.append(i*i)
#for i in range(len(a)):
# print {a[i*2] : a [i*2+1] for i in range(0,len(a)/2) }
# print a
# d = {}
# for i in range(0,input()):
# 	d.insert(i,i**i)
d = {}
for i in range(1,input()+1):
 	d[i] = i*i
print d
print list(d)
print tuple(d)
	