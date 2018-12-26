"""
A simple coffee machine.
"""
# Ingredients
class Ingredient:
    """Abstract class"""
    NAME = 'nothing'

class Water(Ingredient):
    NAME = 'water'

class Milk(Ingredient):
    NAME = 'milk'

class CoffeeBean(Ingredient):
    NAME = 'coffee_bean'

class Recipe:
    def __init__(self, ingredients):
        """
        :param ingredients: a tuple of (ingredient, quantity)
        """
        self.ingredients = ingredients

# Products
class BaseCoffee:
    """Abstract class"""
    RECIPE = None
    NAME = "nothing"

    def print(self):
        print("This is a cup of {}".format(self.NAME))

class PlainCoffee(BaseCoffee):
    RECIPE = Recipe(((Water(), 10), (CoffeeBean(), 1)))
    NAME = 'Pure coffee'

class MilkCoffee(BaseCoffee):
    RECIPE = Recipe(((Water(), 10), (CoffeeBean(), 1), (Milk(), 1)))
    NAME = 'Milk coffee'

class CoffeeMachine:
    def __init__(self):
        self._inventory = {}    # Dictionary. Ingredient -> quantity

    def add_ingredient(self, ingredient_cls, quantity):
        self._inventory[ingredient_cls.NAME] = quantity + self._inventory.get(ingredient_cls.NAME, 0)

    def remove_ingredient(self, ingredient, quantity):
        curr = self._inventory.get(ingredient.NAME)
        if curr is None or curr < quantity:
            print("The existing quantity is less than the requested value.")
            return
        self._inventory[ingredient.NAME] = curr - quantity

    def brew(self, coffee_cls):
        if not self._check_availabilities(coffee_cls):
            print("Not enough ingredient. Not possible to brew the current selection")
            return
        return self._brew_helper(coffee_cls)

    def _check_availabilities(self, coffee_cls):
        for ingredient, quantity in coffee_cls.RECIPE.ingredients:
            curr = self._inventory.get(ingredient.NAME)
            if curr is None or curr < quantity:
                return False
        return True

    def _brew_helper(self, coffee_cls):
        for ingredient, quantity in coffee_cls.RECIPE.ingredients:
            self._inventory[ingredient.NAME] -= quantity

        return coffee_cls()


if __name__ == '__main__':
    cm = CoffeeMachine()
    cm.add_ingredient(Water, 20)
    cm.add_ingredient(Milk, 2)
    cm.add_ingredient(CoffeeBean, 2)
    c = cm.brew(PlainCoffee)
    if c is not None:
        c.print()
    c = cm.brew(MilkCoffee)
    if c is not None:
        c.print()
    c = cm.brew(MilkCoffee)
    if c is not None:
        c.print()
