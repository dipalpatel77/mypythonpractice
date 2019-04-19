# file two.py
import one

print("5 top-level in two.py")
one.func()

if __name__ == "__main__":
    print("6 two.py is being run directly")
    print "Hello World from %s!" % __name__
else:
    print("7 two.py is being imported into another module")
