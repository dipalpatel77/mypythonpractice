# a = set('HackerRank')
# b = set('dipalpatel')
# print a,b
# a.add(3)
# print "after adding", a
# c = set()
# c =a.copy()
# print c
# print "difference " ,a.difference(b)
# print "difference update removes the element from b ", a.difference_update(c)
# print "removes the element if it is the member of this set",a.discard(b),a
# print "returns a new et after intersection",c
# d= b.intersection(a,c)
# b.add(4)
# print d
def average(array):
    s = 0
    st = set(array)
    age = 20
    name = 'dipalpatel'
    print ("<{0}> is of /</{1}>".format(name,age))
    x =len(st)
    for i in range(len(st)):
        s+=st.pop()
    s = float(s/x)       
    return s
    # your code goes here
a = [1,2,3,4,5]
print (average(a))
