#!/usr/bin/env python3

import sys


def key_by_value(dic, dict_val):
    for key, value in dic.items():
        if value == dict_val:
            return key
    return None


def check(val):
    if not val:
        return
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
    new_val = val.title()
    if new_val in states.keys():
        print("{} is the capital of {}".format(capital_cities[states[new_val]], new_val))
    elif new_val in capital_cities.values():
        print("{} is the capital of {}".format(new_val, key_by_value(states, key_by_value(capital_cities, new_val))))
    else:
        print("{} is neither a capital city nor a state".format(val))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        for i in sys.argv[1].split(','):
            check(i.strip())
