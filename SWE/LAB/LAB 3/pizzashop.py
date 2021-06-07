from pizza import Pizza, PizzaSize, PizzaToppings


# This function shows a limitation on tool-assisted
# refactoring in a dynamic language like Python.
#
# When you rename the Pizza getPrice method to get_price,
# does it rename the method here?
# - if no type annotation on the pizza parameter, maybe not
# - if use type annotation ':Pizza' on the parameter, it should

def print_pizza(pizza):
    """
    Print a description of a pizza, along with its price.
    """
    print(pizza)


if __name__ == "__main__":
    pizza = Pizza(PizzaSize.small)
    pizza.add_topping(PizzaToppings.mushroom)
    pizza.add_topping(PizzaToppings.tomato)
    pizza.add_topping(PizzaToppings.pineapple)
    print_pizza(pizza)

    pizza2 = Pizza(PizzaSize.medium)
    print_pizza(pizza2)

    pizza3 = Pizza(PizzaSize.large)
    pizza3.add_topping(PizzaToppings.seafood)
    print_pizza(pizza3)
