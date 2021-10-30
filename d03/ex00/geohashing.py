#!/usr/bin/env python3

from sys import argv
from antigravity import geohash as ghash

if __name__ == '__main__':
    if len(argv) != 4:
        print('Wrong numbers of arguments')
        exit(1)
    try:
        ghash(float(argv[1]), float(argv[2]), argv[3].encode())
    except Exception as exc:
        print(exc)
        exit(1)
