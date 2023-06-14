#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for i in my_list:
        if i != search:
            new.append(i)
        else:
            new.append(replace)
    '''
    new = list(map(lambda x: replace if x == search else x, my_list))
    '''
    return new
