#!/usr/bin/env python3
# -*- coding: utf-8 -*-




def min_max(*args):
    # Результат
    composition = 1
    # Индекс и item для максимального
    max_arg = args[0]
    max_ind = 0

    # Индекс и item для минимального
    min_arg = args[0]
    min_ind = 0
    # Проходит по списку и вычисляет max и min
    for i, item in enumerate(args):
        if item > max_arg:
            max_arg = item
            max_ind = i
        if item < min_arg:
            min_arg = item
            min_ind = i
    for i in args[min_ind:max_ind]:
        composition *= i
    return composition


if __name__ == '__main__':
    arg = list(map(float, input('Введите список аргументов: ').split()))
    print("Произведение аргументов, расположенных"
          " между максимальным и минимальным аргументами:  ",
          min_max(*arg))
    if not arg:
        print("None")