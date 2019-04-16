def compare(a,b):
    for i in range(len(a)):
        for k in range(len(b)):
            if a[i]==b[k]:
                print("the no is same")
                print(a[i],+b[k])
            else:
                print("not found ")




a=[1,2,3,4,5]
b=[1,2,3,4,5]
compare(a,b)