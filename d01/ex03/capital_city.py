#!/usr/bin/env python3

import sys


def what_cap_city(state):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    return capital_cities.get(states.get(state))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        res = what_cap_city(sys.argv[1])
        if not res:
            print("Unknown state")
        else:
            print(res)
