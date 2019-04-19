def find(a):
        for i in range(len(numbers)):
                for j in range(1,len(numbers)):
                    if numbers[j]<numbers[i]:
                            temp=numbers[i]
                            numbers[i]=numbers[j]
                            numbers[j]=temp
                            j=j+1
                    else:
                        i+1



numbers=[43,6,5,43,4,43,534,5,34]
find(numbers)
print(numbers)
