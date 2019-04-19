class dipal:
    global cd
    cd = 38
    def __init__(self):
        print ("hello constructor first")
    def __init__(self,a,b):
        print('firstconstructor')
        self.a=a
        self.b=b
        print (a,b)
        print (self.a,self.b)
        print (a*b)
    def ocheck(self, a, b):
        print ('ocheck')
        #self.e = a
        #self.f = b
        print(a, b)
        print(b + b)
        print(a + b)
        print(cd)
    def sum(self, aAN, bAn):
        print('sum')
        print (self.a,self.b)
        #print (a,b)
        self.x = aAN
        self.y = bAn
        print (aAN, bAn)
        #return self.a + self.b
    def additon(self,):
        print ('d.addition()')
        print (self.x + self.y)



d = dipal(3,3)
d.ocheck( 4, 5)
print ("cd=",cd)
print (d.sum(45,5))
d.additon()
