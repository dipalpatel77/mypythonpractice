def checknum(self):
    isodd = False
    a = list(map(int,self))
    nsum = 0
    for i in range(len(a)):
        if(isodd):
            a[i] = a[i] * 2
        isodd = ~ (isodd)
        nsum += int( a[i] / 10)
        nsum += int( a[i] % 10)
    if(nsum % 10 == 0):
        print("the is valid")
    else:
        print("it's not valid")

c = True
while(c):
    try:
        a = input("enter numbers : ")
        if(a.isdigit):
            b = list(map(int,a))
            b.reverse()
            checknum(b)
            d = input("do you want to continue 'y' for yes 'n' for no : ")
            if(d == 'y'):
                c = True
            else:
                break;
    except ValueError:
        print("invalid input type numbers only")
        c = True
