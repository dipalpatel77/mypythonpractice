# # Enter your code here. Read input from STDIN. Print output to STDOUT
# b = [raw_input() for i in range(input())]
# b = set(b)
# print len(b)
#--------------
# country = set([raw_input() for i in range(int(input()))])
# print(len(country))
# -------------------
li=set()
for i in range(int(input())):
    li.add(raw_input())
print(len(li))