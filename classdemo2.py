__author__ = 'DIPAL'
class inside:  
    x=388
    y=3298
    def __init__(self):
        print"called:",type(self)
       # print(x)
        pass
    def addition(self, a, b):
        print"sum=",a + b
    def subtracton(self, a, b):
        print "sub=",a - b
        return 0
    def main(self):
      a = int(input("enter the value of a"))
      b = int(input("enter the value of b"))
      print " ".join(raw_input()) 
      ic=inside()
      print(ic.addition(a, b))
      print(ic.subtracton(a, b))
class demoforadditoin(inside):
    def __init__(self):
        d=inside()
        print(d.x)
        print(d.y)
        d.main()
        d.addition(32,23)
        d.subtracton(32,23)
           
class inherits(demoforadditoin,inside):
    def __init__(self):# it is the constructor so it'll get automatically called on creating object of inherit
        i=demoforadditoin()
        j=inside()
                

d=inherits()
#p=inside()
#p.foo()
#d.main()
#print d.x
#print d.y
#d=inherits()
