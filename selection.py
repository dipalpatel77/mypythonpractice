import datetime
class Selection(object):
    """docstring for Selection."""

    def __init__(self, arg):
        super(Selection, self).__init__()
        self.arg = arg
    def setDate(self,day,month,year):
        """ this is the docstring"""
        self.day = day
        self.month = month
        self.year = year
    def Userinput(self,):
        """this is docstring for Userinput it takes user raw_input
           and also also calls the display fucntion to assing the
           values """
        day = raw_input("enter day")
        month = raw_input("enter month")
        year = raw_input("enter year")
        obj.setDate(day,month,year)
    def Display(self,):
        print(obj)
        print (self.day,self.month,self.year)
if __name__ == "__main__":
    obj = Selection('morning')
    obj.Userinput()
    #obj.setDate(day,month,year)
    obj.Display()
    print(obj.Userinput.__doc__)
    print("successfuly run")
