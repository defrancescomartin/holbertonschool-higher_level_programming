#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolean = []
    for i in my_list:
        if i % 2 == 0:
            boolean.append(True)
        else:
            boolean.append(False)

    return boolean
