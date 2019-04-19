<<<<<<< HEAD
# from numpy import *
# a = array([[2,3], [4,5]])
# b = array([[1,2], [3,0]])
# print a
# print b
# print a + b
# print a * b
m = [[1,2],[3,4],[5,6]]
for row in m :
    print(row)
print (len(m))
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
print (len(rez))
for row in rez:
    print(row)
=======
from numpy import *
a = array([[2,3], [4,5]])
b = array([[1,2], [3,0]])
print a
print b
print a + b
print a * b
>>>>>>> origin/master
