#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    index = [range((len(my_list)-1), -1, -1)]
    for i in index:
        print('{:d}'.format(my_list[i]))
