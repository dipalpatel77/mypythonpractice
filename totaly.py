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
