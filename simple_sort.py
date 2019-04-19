def sorts(a):
     for i in range(len(a)):
         if(a[i+1]>a[i]):
             temp=a[i]
             a[i]=a[i+1]
             a[i+1]=temp
             print(a)
         else:
             break
     


for i in range(len(a)):
	if a[i]>20:
		print i ,":",  a[i]
