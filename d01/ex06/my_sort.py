#!/usr/bin/env python3

def make_dict():
    return {
        'Hendrix': '1942',
        'Allman': '1946',
        'King': '1925',
        'Clapton': '1945',
        'Johnson': '1911',
        'Berry': '1926',
        'Vaughan': '1954',
        'Cooder': '1947',
        'Page': '1944',
        'Richards': '1943',
        'Hammett': '1962',
        'Cobain': '1967',
        'Garcia': '1942',
        'Beck': '1944',
        'Santana': '1947',
        'Ramone': '1948',
        'White': '1975',
        'Frusciante': '1970',
        'Thompson': '1949',
        'Burton': '1939',
    }


if __name__ == '__main__':
    dic = make_dict()
    # for i in sorted(dic.items(), key=lambda para: (para[1], para[0])):
    #     print(i[0])
    lst = []
    for i in dic.items():
        lst.append((i[1], i[0]))
    lst.sort()
    for i in lst:
        print(i[1])
