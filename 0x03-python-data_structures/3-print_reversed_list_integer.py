#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        print('', end='')
    else:
        my_list.reverse()
        for i in my_list[:: -1]:
            print(f"{my_list[i]}")
