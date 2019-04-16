def encrypt(msg,key,l):
    for i in(z):
        if ord(i)>=97 and ord(i)<= 122:
            if ord(i)+key > 122:
                p=chr(ord(i)+key-26)
                l.append(p)
            else:
                p=chr(ord(i)+key)
                l.append(p)
        elif ord(i)>=65 and ord(i)<= 90:    
            if ord(i)+key > 90 :
                p=chr(ord(i)+key-26)
                l.append(p)
            else:
                p=chr(ord(i)+key)
                l.append(p)       
def decrypt(msg,key,l):
    print key
    for i in(x):
        if ord(i)>=97 and ord(i)<= 122:
                if ord(i)-key <97:
                    p=chr(122-ord(i)+97-key)
                    l.append(p)
                else:
                    #print 'its here'
                    p=chr(ord(i)-key)
                    #print p
                    l.append(p)
        elif ord(i)>=65 and ord(i)<= 90:
            if ord(i)-key > 65 :
                p=chr(ord(i)-key+26)
                l.append(p)
            else:
                p=chr(ord(i)-key)
                print chr(ord(i)-key)
        else :
            print chr(ord(i)-key)

z=input("enter the string")
l=list()
print ''.join(str(e) for e in l)
key = input("enter the key")
encrypt(z,key,l)
print " ".join(str(x) for x in l)
print l
li=list()
x= input("enter to decrypt")
decrypt(x,key,li)
print li
print ''.join(str(e) for e in li)