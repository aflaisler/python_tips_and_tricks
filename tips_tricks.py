from __future__ import division
import pandas as pd
import numpy as np
import json
import collections
import random
import heapq
from pandas_summary import DataFrameSummary
import itertools
pd.set_option('display.max_columns', None)


# cPickle
# to save something
with open('model.pkl', 'w') as f:
    pickle.dump(model, f)
# to reload
with open('model.pkl') as f:
    model = pickle.load(f)
# (model.predict(...))

# EDA made easy
dfs = DataFrameSummary()
dfs.columns_stats()
# or
df.describe()

# non unique elements in list
non_unique = [item for item, count in Counter(lst).items() if count > 1]

# list to str
''.join(list)

# decorator


def decorator(func):
    def wrap(text):
        return "<h1>" + func(text) + "</h1>"
    return wrap


@decorator
def do_something(text):
    return text + text


# reverse list
lst[::-1]

# lambda fct
# for example: map(g, lst)
g = lambda x: x**2

# apply vs apply map vs map
apply works on a row / column basis of a DataFrame
applymap works element - wise on a DataFrame
map works element - wise on a Series

# read text
with open('alice.txt', 'r') as f:
    for line in f:
        for word in line.split():
            print(word)
with open('alice.txt') as f:
    x = [line.split() for line in f]
with open('alice.txt') as f:
    x = [word for line in f for word in line.split()]

# exceptions (for example: raise ImportError("error text"))
ImportError: an import fails
IndexError: a list is indexed with an out - of - range number
NameError: an unknown variable is used
SyntaxError: the code can't be parsed properly
TypeError: a function is called on a value of an inappropriate type
ValueError: a function is called on a value of the correct type, but with an inappropriate value

# extended unpacking (py3)
a, *b, c = [1, 2, 3, 4, 5]

# format function
for i, x in enumerate(a):
    print '{}: {}'.format(i, x)

# Inverting a dictionary using zip
mi = dict(zip(m.values(), m.keys()))

# Flattening lists
[x for l in lst for x in l]
flatten(lst)

# set and set operations
A = set(range(5))
B = set(range(4, 10))
A - B
A | B

# Most common elements in an iterable (collections.Counter) &
# collections.defaultdict
A = Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
A.most_common(1)
m = collections.defaultdict(str)

# Using default dictionaries to represent simple trees
tree = lambda: collections.defaultdict(tree)
root = tree()
root['menu']['id'] = 'file'
root['menu']['value'] = 'File'
root['menu']['menuitems']['new']['value'] = 'New'
root['menu']['menuitems']['new']['onclick'] = 'new();'
print json.dumps(root, sort_keys=True, indent=4, separators=(',', ': '))

# Largest and smallest elements (heapq.nlargest and heapq.nsmallest)
a = np.random.randint(0, 100, size=100)
print heapq.nsmallest(5, a)
print heapq.nlargest(5, a)

# Combinations, combinations with replacement, Permutations
for c in itertools.combinations([1, 2, 3, 4, 5], 3):
    print ''.join(str(x) for x in c)

for c in itertools.combinations_with_replacement([1, 2, 3], 2):
    print ''.join(str(x) for x in c)

for p in itertools.permutations([1, 2, 3, 4]):
    print ''.join(str(x) for x in p)


# min max of rest of array
[min([a for a in array[i + 1:] if a > array[i]], default=-1)
 for i in range(len(array))]

# The zen of python
import this

# python debugger
import pdb
pdb.set_trace()
# then add this "pdb.set_trace()" where you want to set trace

# Draw graphs (ipython)
import matplotlib.pyplot as plt  # Standard Python Library for working with graphs
import networkx as nx  # Helper library to visualize graphs
import nxpd
plt.style.use('ggplot')

g_adj = {
    0: {1, 4},
    1: {0, 2, 3},
    2: {1, 3, 5},
    3: {1, 2, 4},
    4: {0, 3, 4},
    5: {2}}

# Draw left to right when possible, fits better in notebook
G = nx.from_dict_of_lists(g_adj)
G.graph['rankdir'] = 'LR'
nxpd.draw(G, show='ipynb')

# To time functions
# Method 0 (iPython)
import timeit
%timeit - n30 - r 4 fact(900)  # return: 30 loops, best of 4: 1.05 ms per loop
# Method 1
import time
t1 = time.time()
math.factorial(900)
t2 = time.time()
print 'math factorial took {} seconds'.format(t2 - t1)
# Method 2
from timeit import Timer
<parameter >  # (for example: 'xrange(100000000, 101000000)')

# Make a list of functions to time.
# callables without args...
funcs = [ < func_1 > , < func_2 > ]
tests = [(test_func.__name__, test_func) for test_func in funcs]

for name, test in tests:
    # We have to do this because Timer takes a callable as an arg.
    t = Timer(lambda: test(< parameter > ))
    print "Completed {name} in {time} seconds.".format(name=name,
                                                       time=t.timeit(1))

# Profiler (requires to be run in the command line with the function in an external .py)
# For example:
# @profile
from memory_profiler import profile


def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    my_func()

# for time
kernprof - lv example.py
# for memory usage
python - m memory_profiler example.py
# to plot memory usage
mprof run < exec.py >
mprof plot

# sorted with lambda for the 'move zeros to the end' pb


def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and type(x) is not bool)
