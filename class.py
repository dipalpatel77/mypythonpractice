class dipal:
    global cd
    cd=38
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print a,b
        print self.a,self.b
        print a*b
    def ocheck(self, a, b):
        self.a = a
        self.b = b
        print(a)
        print(b + b)
        print(a + b)
        print(cd)
    def sum(a, b):
        return a + b


d = dipal(4,5)
d.ocheck( 4, 5)
print ("cd=",+cd)
