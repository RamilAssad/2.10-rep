#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def Garm(*args):
    if args:
        values = [float(arg) for arg in args]
        values.sort()

        a = 0
        n = len(values)
        for i in values:
            a = a + (1 / i)
        return n / a
    else:
        return None

if __name__ == "__main__":
    print(Garm())
    print(Garm(1,2,3,4,5))