a = []
for i in range(10):
    a.append(int(input()))
    

a.sort()
a.reverse()
#print a
total1= a[0]+a[2]+a[4]
total2= a[1]+a[3]+a[5]
#print total1 , total2
if total1 > total2:
    print total1
else:
    print total2