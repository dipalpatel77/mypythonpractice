# N, M = map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
# for i in xrange(1,N,2):
#     print ((M-i)*'-')+ (i*'-|-') +((M-i) *'-')
# print ((M-8)*'-')+"WELCOME"+((M-8)*'-') 
# # for i in xrange(N-2,-1,-2): 
# #     print 

N, M = map(int,raw_input().split())
for i in range(0,N):
    l = 'Dipal' if i == int(N/2) else ('.|.'*(N-(2*abs(i-int(N/2)))))          
    print(l.center(M,'-'))