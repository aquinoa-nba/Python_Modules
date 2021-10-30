#!/usr/bin/env python3

import sys


def key_by_value(dic, dict_val):
    for key, value in dic.items():
        if value == dict_val:
            return key
    return None


def what_state(cap_val):
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
    res = key_by_value(states, key_by_value(capital_cities, cap_val))
    if not res:
        print("Unknown capital city")
    else:
        print(res)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        what_state(sys.argv[1])
