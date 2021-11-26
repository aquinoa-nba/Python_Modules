#!/usr/bin/env python3

import beverages
import random


class CoffeeMachine:
    def __init__(self):
        self.after_repair = 0

    class EmptyCup(beverages.HotBeverage):
        def __init__(self, price=0.90, name='empy cup'):
            super().__init__(price, name)

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.after_repair = 0

    def serve(self, hot_beverage):
        if self.after_repair < 10:
            self.after_repair += 1
            if random.randint(0, 1):
                return hot_beverage
            return self.EmptyCup()
        raise self.BrokenMachineException()


if __name__ == '__main__':
    machine = CoffeeMachine()
    beverages_lst = [
        beverages.HotBeverage(),
        beverages.Coffee(),
        beverages.Tea(),
        beverages.Chocolate(),
        beverages.Cappuccino()
    ]
    for i in range(23):
        try:
            print(machine.serve(beverages_lst[random.randint(0, 4)]).description())
        except machine.BrokenMachineException as exc:
            print('\n', exc, '\n', sep='')
            machine.repair()
