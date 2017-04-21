from __future__ import division
import pandas as pd
import numpy as np
import json
import collections
import random
import heapq
from pandas_summary import DataFrameSummary
import pdb
pd.set_option('display.max_columns', None)


# merge sort
lst = list(np.random.randint(100, size=10))


def sort(lst):
    n = len(lst) // 2
    if len(lst) > 1:
        lst_1 = lst[:n]
        lst_2 = lst[n:]
        ord_lst_1 = sort(lst_1)
        ord_lst_2 = sort(lst_2)
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


# Pyramid Slide Down (Acyclic graphs and critical paths)
tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]


def longestSlideDown(tri):
    while len(tri) > 1:
        n = len(tri) - 1
        x = tri.pop(n)
        y = tri.pop(n - 1)
        tri.append([max(y[i] + x[i], y[i] + x[i + 1]) for i in range(len(y))])
        # print tri
    return tri[0].pop()
