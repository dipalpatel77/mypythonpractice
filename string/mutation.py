
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
i, c = raw_input().split()

print s[:int(i)] + c + s[int(i)+1:]