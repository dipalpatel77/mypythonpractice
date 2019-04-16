a = int(input("enter the no:"))
c = []
if a == 0:
  print("not valid")
else:
  fact = 1
  for i in range(1, a + 1):
    fact *= i
    c.append(fact)


print(c)
print (c[len(c)-1])