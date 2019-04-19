def check(a, b, c):
  if a in range(b):
    if b in range(c):
      print 'range c', + a,b
      return
    else:
      print(a, b, c)
      return 0

  else:
    print("\n", a)
    return 0



check(4, 5, 8)
a = list()
print(type(a))