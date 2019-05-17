class Dipal:
    """the test class for evrything."""
    global cd
    cd = 38
    insum = 23

    def __init__(self):
        """This is the constructor defined first"""
        print("hello constructor first")

    def __init__(self, a, b):
        """the second constructor defined second"""
        print('firstconstructor')
        self.a = a
        self.b = b
        print(a, b)
        print(self.a, self.b)
        print(a * b)

    def ocheck(self, a, b):
        """prints the sum of a and b also product of a and b"""
        print('ocheck')
        # self.e = a
        # self.f = b
        print(a, b)
        print(b + b)
        print(a + b)
        print(cd)

    def sum(self, aAN, bAn):
        """another function called sum wich also prints sum and multiplication"""
        insum = 32
        print('sum')
        print(self.a, self.b)
        # print (a,b)
        self.x = aAN
        self.y = bAn
        print(aAN, bAn)
        # return self.a + self.b

    def additon(epd, ):
        """this is another addition class that doesnt take any arguments but
            does the exactly same thing."""
        print('d.addition()')
        print(epd.x + epd.y)


if __name__ == '__main__':
    """this is the main fucntion of the python everything starts from here"""
    d = Dipal(3, 3)
    print("second object --------------------------------")
    e = Dipal(3.12, 4)
    print("comapre the object ---------------------------")
    print(d == e)

    d.ocheck(4, 5)
    d.insum = 52
    print("cd=", Dipal.insum, d.insum)
    print(d.sum(45, 5))
    d.additon()
