#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    k = 0
    p = 0
    new_list = []
    for k in range(0, list_length):
        try:
            p = (my_list_1[k] / my_list_2[k])
        except TypeError:
            p = 0
            print("wrong type")
        except ZeroDivisionError:
            p = 0
            print("division by 0")
        except IndexError:
            p = 0
            print("out of range")
        finally:
            new_list.append(p)
    return new_list
