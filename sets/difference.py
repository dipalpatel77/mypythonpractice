# Enter your code here. Read input from STDIN. Print output to STDOUT
K = raw_input() 
M = set(map(int,raw_input().split()))
H = raw_input()
N = set(map(int,raw_input().split()))
Sol = sorted(list(M.difference(N)) + list(N.difference(M))) 
for i in Sol:
    print i
