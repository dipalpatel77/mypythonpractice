b = list()
c = 0
d = 0

a = int(input())
for i in range(a):
  bx = map(int, input().split())
  b.append(bx)
  # c=sum(b)
y = len(b) - 1
print(y)
for i in range(len(b)):
  print(i, y)
  c = c + b[i][i]
  print(b[i][y])
  d = d + b[i][y]
  y = y - 1
b = list()
print(c, +d)
print(y)
print("the difference is=", +c - d)

'''' def getDiagonalDifference(v):
    diff = 0
    v_len = len(v)
    for idx in xrange(v_len):
        diff += v[idx][idx]
        diff -= v[idx][v_len-idx-1]
 
    return abs(diff)    
         
if __name__ == '__main__':
    t = input()
    v = []
    for _ in xrange(t):
        e = map(int, raw_input().split())
        v.append(e)
         
    print getDiagonalDifference(v)  '''
