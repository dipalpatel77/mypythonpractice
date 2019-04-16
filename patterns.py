def draw_pattern(s):
    k=0
    for i in range(len(s)):
        for j in range(1,len(s)-1):
            print("")
        for k in range(0,k<=i):
            print(s[k])


s="dipal"
draw_pattern(s)
