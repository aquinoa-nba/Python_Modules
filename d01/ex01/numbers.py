#!/usr/bin/env python3

def print_nums():
    f_in = open("numbers.txt")

    for nbr in f_in.read().split(','):
        print(nbr, end="")
        if nbr[-1] == '\n':
            continue
        print()
    f_in.close()


if __name__ == '__main__':
    print_nums()
