# def simple(k):
# 	my = []
# 	for i in range(1,6):
# 		x = i* k
# 		my.append(x)
# 	return my

# a = simple(5)
# print (a)
def _list_of_multiples_sample_(k):
    my_list = []
    for i in range(1, 6):
        multiple = k * i
        my_list.append(multiple)
    return my_list

print (_list_of_multiples_sample_(5))