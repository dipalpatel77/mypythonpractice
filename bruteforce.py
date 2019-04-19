def encrypt(msg,key):
    for i in(z):
        if ord(i)>=97 and ord(i)<= 122:
            print 'upto here!'
            if ord(i)+key > 122:
                print chr(ord(i)+key-26)
            else:
                print 'its else'
                print chr(ord(i)+key)
        elif ord(i)>=65 and ord(i)<= 90:
            print 'less then 90'
            if ord(i)+key > 90 :
                print chr(ord(i)+key-26)
            else:
                print chr(ord(i)+key)
        else :
            print chr(ord(i)+key)

a=list()
