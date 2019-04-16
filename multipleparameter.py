__author__ = 'DIPAL'
def multiparameter(*a):
    print a

for i in range(3):
  a=map(multiparameter,raw_input().split())
multiparameter(a) 