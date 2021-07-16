

def print_type(variable):
    """This function prints the type of supplied variable

    Args:
        variable (Any): variable to print type for
    """
    # fill the gaps ...
    x = type(variable)
    return print(x)


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
    if isinstance(variable, int):
        variable = variable * variable
        return print(variable)
    elif isinstance(variable, float):
        return print(variable + math.pi)
    elif isinstance(variable, bool):
        return print(not variable)
    elif isinstance(variable, list):
        arr = variable[::-1]
        return print(arr)
    else:
        return print("Action is not defined")


variables = [42, 45.0, True, False, [16, 9, 43, 65, 97, 0]]

# Please, for all elements in `variables` list print the following:
#  the type of variable using `print_type` function
#  and the action for variable using `do_action` function

for i in variables:
    print_type(i)
    do_action(i)