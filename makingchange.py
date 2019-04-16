class mack:
       def makingchange(self,a,num):
        x=[]
        rem=num
        d=len(a)
        while(rem>0):
            if(rem>=a[d-1]):
                x.append(a[d-1])
                rem=rem-a[d-1]
            else:
                d-=1
        print(x)
        print(rem)
c=[1,2,5,10,50,100,500,1000]
#for i in range(4):
    #c.append(int(raw_input("enter the coins you have ")))
x=input("enter the no")
print "coins that we have=",c
print("change made for =",x)
d=mack()
d.makingchange(c,x)
    
            
