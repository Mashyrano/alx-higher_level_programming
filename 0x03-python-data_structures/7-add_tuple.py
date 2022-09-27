#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        a = tuple_a[0]
        b = tuple_a[1]
    elif len(tuple_a) == 1:
        a = tuple_a[0]
        b = 0
    else:
        a = 0
        b = 0
    if len(tuple_b) >= 2:
        a1 = tuple_b[0]
        b1 = tuple_b[1]
    elif len(tuple_b) == 1:
        a1 = tuple_b[0]
        b1 = 0
    else:
        a1 = 0
        b1 = 0
    new_tuple = (a + a1, b + b1)
    return new_tuple
