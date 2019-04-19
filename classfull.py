__author__ = 'DIPAL'
class demoforadditoin:
        x=388
        _y=3298
        def __init__(self):
                print"called:",type(self)                
                pass
        def addition(self, a, b):
              print"sum=",a + b
              self.a = 10
              self.b = 22
              print self.a +self.b
        def subtracton(self, a, b):
              print "sub=",a - b
              return 0
        def main(self):
                a = int(input("enter the value of a"))  
                b = int(input("enter the value of b"))
                d = demoforadditoin()
                print(d.addition(a, b))
                print(d.subtracton(a, b))
class fool:
        x=demoforadditoin()
        t=x.main()
        y=list()
        print("t",t)
        y.append(t)
        print(y)
        def __init__(self):
                y=demoforadditoin()
                y.main()

    

#d=demoforadditoin()
#d.main()
#print d.x
#print d.y
d=fool()
