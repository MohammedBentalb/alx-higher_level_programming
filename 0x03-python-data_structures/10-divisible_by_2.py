#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''
ONE WAY OF DOING IT
    new = []
    for i in my_list:
        new.append(True if i % 2 == 0 else False)
    return new
    '''

    new = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
