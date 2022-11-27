#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def first_last(*args):
    composition = 1
    last_arg = args[0]
    last_ind = 0
    first_arg = args[0]
    first_ind = 0
    for i, item in enumerate(args):
        if item > last_arg:
            last_arg = item
            max_ind = i
        if item < first_arg:
            min_arg = item
            min_ind = i
    for i in args[first_ind:last_ind]:
        composition *= i
    return composition


if __name__ == '__main__':
    arg = list(map(float, input('Введите список аргументов: ').split()))
    print("Произведение аргументов, расположенных"
          " между первым и последним аргументами:  ",
          first_last(*arg))