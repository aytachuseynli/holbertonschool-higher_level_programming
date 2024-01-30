#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = []
    for item in my_list:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements
