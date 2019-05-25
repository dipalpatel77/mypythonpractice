# a.difference(b)  or a - b  != b.difference(a) or b - a
from pip._vendor.distlib.compat import raw_input

a = input()
s = set(map(int,raw_input().split()))
b =input()
k = set(map(int,raw_input().split()))
print (len(s.difference(k)))