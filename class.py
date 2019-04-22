class dipal:
    global cd
    cd = 38
    insum = 23
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
        insum = 32
        print('sum')
        print (self.a,self.b)
        #print (a,b)
        self.x = aAN
        self.y = bAn
        print (aAN, bAn)
        #return self.a + self.b
    def additon(epd,):
        print ('d.addition()')
        print (epd.x + epd.y)



d = dipal(3,3)
d.ocheck( 4, 5)
d.insum = 52
print ("cd=",cd,dipal.insum,d.insum)
print (d.sum(45,5))
d.additon()
