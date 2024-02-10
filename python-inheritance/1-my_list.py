#!/usr/bin/python3
"""
print ascending sorted list
"""


class MyList(list):
    """
    MyList is a subclass of the built list class
    with an additional method.
    """

    def print_sorted(self):
    """
    Sorts the list in ascending order using 
    the built-in sort method and prints 
    the sorted list.
    """

    print(sorted(self))
