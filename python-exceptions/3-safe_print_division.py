#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
        print("Inside result: {}\n{} / {} = {}".format(result, a, b, result))
    except (ZeroDivisionError, TypeError) as e:
        print("An error occurred:", e)
        return None
    finally:
        print("Finally block: Division operation completed.")
    return result
