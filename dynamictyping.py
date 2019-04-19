jobs = {
    int: lambda x, y: x ** 2 + y,
    str: lambda x, y: y.join(x.split())
    list: lambda x, y: [min(x), max(x), min(y), max(y)]
}


def something(a, b):
    if type(a) != type(b):
        raise Exception('Arguments not of the same type')
    if not jobs.has_key(type(a)):
        raise Exception('Don\'t know how to handle this type')
    return jobs[type(a)](a, b)


print(something(4, 5))
print(something("This is so useless.", " ... "))
print(something([5, 3, 11, 9, 7], [20, 16, 8, 24, 14, 18]))
