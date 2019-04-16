# file one.py
def func():
    print(" 1 func() in one.py")
    print "Hello World from %s!" % __name__

print("2 top-level in one.py")

if __name__ == "__main__":
    print(" 3 one.py is being run directly")
    print "Hello World from %s!" % __name__
else:
    print(" 4 one.py is being imported into another module")


