def print_formatted(number):
    n = str(bin(number))
    s = len(n)
    n2 = str(hex(number))
    n3 = str(oct(number))
    n4 = str(number)
    s2 = len(n2)
    s3 = len(n3)
    s4 = len(n4)

    for i in range(1, number+1):
        print "  "+str(i).rjust(s4, " ")+"  "+str(oct(i)).lstrip('0').rjust(s3, " ")+"  "+str(hex(i)).upper().lstrip('0X').rjust(s2-1, " ")+str(bin(i)).lstrip('0b').rjust(s-1, " ")

print_formatted(19)