#!/usr/bin/env python3

import sys
import re
import settings


def func(file, filename):
    f_in = open(file, 'r')
    data = f_in.read()
    f_in.close()
    dic = vars(settings)
    for i in dic:
        data = re.sub("{" + str(i) + "}", str(dic[i]), data)
    f_out = open(filename, 'w')
    f_out.write(data)
    f_out.close()


if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            match = re.search(".template", sys.argv[1])
            if match and match.end() == len(sys.argv[1]):
                func(sys.argv[1], sys.argv[1].replace(".template", ".html"))
            else:
                print("Invalid template format")
        else:
            print("Invalid number of arguments")
    except:
        print(sys.exc_info()[1])
