seq=('year','name','age')	
val = (3,2,1)
a ={}
for i in range(len(seq)):
	a[seq[i]]=val[i]
print seq
print val
print a

a ={}
for i in range(len(seq)):
	a[val[i]]=seq[i]
print seq
print val
print a
''' here the intended dictionary automatically gets sorted by keys'''