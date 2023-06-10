#!/usr/bin/python3
'''new_string = my_string.translate({ord(i): None for i in 'cC'})'''


def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i != "c" and i != "C":
            new_string += i
    return new_string
