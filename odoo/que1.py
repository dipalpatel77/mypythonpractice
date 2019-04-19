'''Write a program which will find all such numbers which are divisible by 7 but
 are not a multiple of 5, between 1000 and 2100 (both included). The numbers obtained
  should be printed in a comma-separated sequence on a single line.'''
x = []
for i in range(1000,2101):
	if i % 7 == 0 and i % 10 != 5:
		x.append(i)
		
print ",".join(map(str,x))
