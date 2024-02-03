#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            # Try to perform the division
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) and my_list_2[i] != 0 else 1  # Avoid division by zero
            result = element_1 / element_2
            result_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
        finally:
            pass  # Optionally, you can include code here that should execute regardless of exceptions

    return result_list
