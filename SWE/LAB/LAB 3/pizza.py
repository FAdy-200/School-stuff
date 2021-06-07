from enum import Enum


class PizzaSize(Enum):
    """
    Enumerator for the sizes with a price function
    """
    small = 0
    medium = 1
    large = 2

    def __str__(self):
        return self.name

    def price(self, toppings: list) -> int:
        """
        calculates the price of the pizza based on its size and toppings choice
        :param toppings: list of PizzaToppings enums
        :return: price
        """
        return PizzaPrice.price(self.name, toppings)


class PizzaToppings(Enum):
    """
    enum class that has topping prices for each topping and size
    """
    mushroom = {'small': 13, 'medium': 15, 'large': 19}
    tomato = {"small": 10, "medium": 12, "large": 16}
    pineapple = {"small": 20, "medium": 22, "large": 18}
    seafood = {"small": 25, "medium": 27, "large": 31}

    def __str__(self):
        return self.name


class PizzaPrice:
    """
    class to calculate the price of the pizza
    """
    sizes = {"small": 120, "medium": 200, "large": 280}

    @staticmethod
    def price(size: str, toppings: list) -> int:
        pr = PizzaPrice.sizes[size]
        for i in toppings:
            pr += i.value[size]
        return pr


class Pizza:
    """A pizza with a size and optional toppings."""
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

    def __init__(self, size: PizzaSize):
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        return self.size.price(self.toppings)

    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def __str__(self):
        """
        :return: description of the pizza
        """
        if self.toppings:
            toppingDescription = "pizza with " + ", ".join(map(str, self.toppings))
        else:
            toppingDescription = "plain pizza"
        description = f"A {self.size} {toppingDescription}"
        price = "Price {:6.2f}".format(self.get_price())
        return description + "\n" + price
