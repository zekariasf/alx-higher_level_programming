#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_l = my_list[0]
    for i in my_list:
        if i > max_l:
            max_l = i
    return max_l
