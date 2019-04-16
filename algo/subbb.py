	# #!/bin/python

# import sys


# n = int(raw_input().strip())
# arr = map(int,raw_input().strip().split(' '))
# #print arr
# a = 0 
# b = 0
# c = 0
# for num in arr:
#     if num > 0:
#         a+=1
#     elif  num < 0:
#         b+=1
#     else:
#         c+=1
# #print a,b,c
# if a > 0:
# 	print ("%.6f" % round(float(a)/len(arr),6))
# if b>0:
# 	print ("%.6f" % round(float(b)/len(arr),6))
# if c>0:
# 	print ("%.6f" % round(float(c)/len(arr),6))

n = int(input().strip())
list1 = [int(x) for x in input().split()]
neg = 0
pos = 0
zer = 0
for x in list1:
    if(x < 0):
        neg+=1
    elif(x > 0):
        pos+=1
    elif(x == 0):
        zer+=1
tot_pos = float(pos)/float(n)
tot_neg = float(neg)/float(n)
tot_zer = float(zer)/float(n)
print("%.6f" % tot_pos)
print("%.6f" % tot_neg)
print("%.6f" % tot_zer)