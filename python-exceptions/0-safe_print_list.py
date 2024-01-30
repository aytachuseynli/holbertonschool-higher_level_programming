#!/usr/bin/python3
def safe_print_list(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeErrror):
        return false
