# def average(array):
#     s = 0
#     x = len(array)
#     print array
#     for i in range(len(array)):
#         s+=array.pop()
#     print s/x 
    
# if __name__ == "__main__":
#     a = set()
#     n = input()
#     for i in range(n):
#         a.add(int(input()))
#     average(a)

def average(array):
    # your code goes here
    s = 0
    st = set(array)
    print st
    x =len(st)  
    for i in range(len(st)):
             s+=st.pop()
    s = float(s)/x      
    return s
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result

#     from statistics import mean
    