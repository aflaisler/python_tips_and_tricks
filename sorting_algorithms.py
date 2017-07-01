from __future__ import division
import pandas as pd
import numpy as np
import json
import collections
import random
import heapq
from pandas_summary import DataFrameSummary
import pdb
from collections import deque
pd.set_option('display.max_columns', None)


# Merge sort (divide and conquer)
lst = list(np.random.randint(100, size=10))


def merge_sort(lst):
    n = len(lst) // 2
    if len(lst) > 1:
        lst_1 = lst[:n]
        lst_2 = lst[n:]
        ord_lst_1 = merge_sort(lst_1)
        ord_lst_2 = merge_sort(lst_2)
        print lst_1, lst_2, ord_lst_1, ord_lst_2
        pdb.set_trace()
        return merge(ord_lst_1, ord_lst_2)
    else:
        return lst


def merge(lst_1, lst_2):
    lst_out = []
    while lst_1 and lst_2:
        if lst_1[0] < lst_2[0]:
            lst_out.append(lst_1[0])
            lst_1.pop(0)
        else:
            lst_out.append(lst_2[0])
            lst_2.pop(0)
    lst_out.extend(lst_1)
    lst_out.extend(lst_2)
    return lst_out


# Quicksort (divide and conquer)

def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[-1]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        # Just use the + operator to join lists
        return sort(less) + equal + sort(greater)
    # Note that you want equal ^^^^^ not pivot
    # You need to hande the part at the end of the recursion - when you only
    # have one element in your array, just return the array.
    else:
        return array
