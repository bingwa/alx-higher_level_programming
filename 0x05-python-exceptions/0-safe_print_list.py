#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    k = 0
    p = 0
    for k in range(0, x):
        try:
            print("{}".format(my_list[k]), end="")
            p += 1
        except:
            continue
    print()
    return p
