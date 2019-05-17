__author__ = 'DIPAL'


class DeluxePizza:
    """ this is the pizza class"""
    cheese_topping = 0
    pepproni_topping = 0
    mushroom_topping = 0
    veggie_topping = 0
    number_of_pizza = 0
    stuffed_with_cheese = True

    def __init__(self, cheese, pepproni, mushroom, veggie, stuffed_or_not):
        self.cheese_topping = cheese
        self.pepproni_topping = pepproni
        self.mushroom_topping = mushroom
        self.veggie_topping = veggie
        self.number_of_pizza = + 1
        self.stuffed_with_cheese = stuffed_or_not
    #
    # def __set__(self, instance, value):
    #     print(" Cheese : ", self.cheese_topping, " mushroom : ", self.mushroom_topping, " veggie : ",
    #           self.veggie_topping, " Number Of pizza : ", self.number_of_pizza, " Stuffed cheese : ",
    #           self.stuffed_with_cheese)
    def Display(self):
        print(" Cheese : ", self.cheese_topping, " mushroom : ", self.mushroom_topping, " veggie : ",
              self.veggie_topping, " Number Of pizza : ", self.number_of_pizza, " Stuffed cheese : ",
              self.stuffed_with_cheese)
