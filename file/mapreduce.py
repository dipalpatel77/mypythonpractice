<<<<<<< HEAD
''' this will print anythng as a string or char'''
c = raw_input("hell ").split()
=======
`c = raw_input().split()
>>>>>>> origin/master
print c, type(c)
d = []
print type(d)
d.append(map(str,c))
print d
print ''.join(map(str,c))
f = int(''.join(map(str,c)))
print type(int(f))

<<<<<<< HEAD
n = int(raw_input("sacond input"))
#integer_list =
print map(int, raw_input("third imput").split())
#print integer_list
=======
n = int(raw_input())
integer_list = map(int, raw_input().split())
>>>>>>> origin/master
