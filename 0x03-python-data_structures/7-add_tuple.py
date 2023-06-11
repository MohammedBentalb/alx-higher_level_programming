#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tmp1 = tuple_a + (0, 0)
    tmp2 = tuple_b + (0, 0)
    new = tmp1[0] + tmp2[0], tmp1[1] + tmp2[1]
    return new
