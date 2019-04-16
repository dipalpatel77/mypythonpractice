`c = raw_input().split()
print c, type(c)
d = []
print type(d)
d.append(map(str,c))
print d
print ''.join(map(str,c))
f = int(''.join(map(str,c)))
print type(int(f))

n = int(raw_input())
integer_list = map(int, raw_input().split())