#!/usr/bin/env python3
if __name__ == '__main__':
    with open('numbers.txt') as f_in:
        for nbr in f_in.read().strip().split(','):
            print(nbr, end="\n")
