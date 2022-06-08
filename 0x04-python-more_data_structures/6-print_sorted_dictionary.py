#!/usr/bin/python3
def print_sorted_dictionary(a_dict):
    for k in sorted(a_dict.keys()):
        print("{}: {}".format(k, a_dict[k])
