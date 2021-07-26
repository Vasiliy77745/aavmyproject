#!/usr/bin/env python3
import math
def print_type(var):
    print(type(var))
def do_action(variable):
    """Does the action depending on variable's type. (hint: you can either use print function right here, 
    or return the result. For now it doesn't matter)
    Defined actions:
        int: square the number
        float: add π(pi) (from math.pi, don't forget the import~!) to it and print the result
        bool: inverse it (e.g if you have True, make it False) and print the result
        list: print elements in reversed order
    Args:
        variable (Any): variable to perform action on
    """
    if isinstance(variable, bool):
         print(not variable)
    elif isinstance(variable, int):
         print(variable * variable)
    elif isinstance(variable, float):
         print(variable + math.pi)
    elif isinstance(variable, list):
        arr = variable[::-1]
        print(arr)
    else:
         print("Action is not defined")


variables = [42, 45.0, True, False, [16, 9, 43, 65, 97, 0]]

for item in variables:
    print_type(item)
    do_action(item)
