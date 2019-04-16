n = input()
s = set(map(int, raw_input().split())) 
a = 0
for i in range(input()):
	command = raw_input().split()
	command[1] = int(command[1])
	if command[0] == 'pop':
		s.pop()
		#print s
	elif command[0] == "remove":
		#print command[0]
		#print command[1]
		if command[1] in s:
			s.remove(int(command[1]))
			#print s
	elif command[0] == "discard":
		if command[1] in s:
			s.discard(int(command[1]))
			#print s
	else:
		print "elif didnt work"
#print s

print sum(s)
#print s