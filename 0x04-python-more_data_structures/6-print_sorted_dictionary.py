#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for i in list_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
    '''
    key = sorted(a_dictionary.keys())
    for elm in key:
        print("{}: {}".format(elm, a_dictionary[elm]))
