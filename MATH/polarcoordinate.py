# Enter your code here. Read input from STDIN. Print output to STDOUTa 
a = raw_input()
for i in range(len(a)):
    if i != '+':
    	b = a[:i]
    	b = float(b)
        print phase(complex(b))
print phase(conplex(a))x,y,z,n = [input() for i in range(4)]
print [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]