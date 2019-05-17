def minion_game(string):
    # your code goes here
    v_count = 0
    new_list = []
    string = string.upper()
    consonent_count = 0
    Vowels = 'aeiou'.upper()
    for i in xrange(len(string)):
        for j in xrange(i , len(string)):
            new_list.append(string[i : j + 1])
    for i in range(len(new_list )- 1 ):
        if new_list[i][0] in Vowels:
            v_count = v_count + 1
        else:
            consonent_count = consonent_count + 1
    if (consonent_count > v_count):
        print "Stuart " , consonent_count
    elif(v_count > consonent_count):
        print "Kevin"  , v_count
    else:
        print "Draw"

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
