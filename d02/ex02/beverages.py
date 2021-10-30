#!/usr/bin/env python3

class HotBeverage:
    def __init__(self, price=0.30, name="hot beverage"):
        self.price = price
        self.name = name

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        res = "name : {}\nprice : {:.2f}\ndescription : {}".format(self.name, self.price, self.description())
        return res


class Coffee(HotBeverage):
    def __init__(self, price=0.40, name='coffee'):
        HotBeverage.__init__(self, price, name)

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self, price=0.30, name='tea'):
        HotBeverage.__init__(self, price, name)


class Chocolate(HotBeverage):
    def __init__(self, price=0.50, name='chocolate'):
        HotBeverage.__init__(self, price, name)

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self, price=0.45, name='cappuccino'):
        HotBeverage.__init__(self, price, name)

    def description(self):
        return "Un po’ di Italia nella sua tazza!"


if __name__ == '__main__':
    beverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()
    print(beverage)
    print(coffee)
    print(tea)
    print(chocolate)
    print(cappuccino)
