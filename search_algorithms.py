import pandas as pd
import numpy as np
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from collections import deque
from itertools import product


# binary search


def bin_search(k, lst):
    n = len(lst) // 2
    if len(lst) > 1:
        lst1 = lst[:n] if k < lst[n] else lst[n:]
        print lst1
        return bin_search(k, lst1)
    else:
        print k, lst
