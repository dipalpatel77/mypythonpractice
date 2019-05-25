import DeluxePizza


class DriverClass:
    cheese_topping = input(" enter the six input ")
    pepproni_topping = input(" enter the six input ")
    mushroom_topping = input(" enter the six input ")
    veggie_topping = input(" enter the six input ")
    number_of_pizza = input(" enter the six input ")
    stuffed_with_cheese = input(" enter the six input ")
    dp = DeluxePizza.DeluxePizza(cheese_topping, pepproni_topping, mushroom_topping, veggie_topping, stuffed_with_cheese)
