#!/usr/bin/python3
def best_score(a_dict):
    return max(a_dict, key=a_dict.get) if a_dict else None
