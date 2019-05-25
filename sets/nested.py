from pip._vendor.distlib.compat import raw_input

lst = [[]]
for _ in range(int(input())):
    lst.append([raw_input(), float(input())])

print (lst)