if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input("name = ")
    if query_name in student_marks:
        print ("%.2f" % sum(student_marks[query_name])/len(student_marks[query_name]))