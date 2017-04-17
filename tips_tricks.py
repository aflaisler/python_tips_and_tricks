from __future__ import division
import pandas as pd
import numpy as np
import json
import collections
import random
import heapq
pd.set_option('display.max_columns', None)

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

# Acyclic graphs and critical paths
while len(pyramid) > 1:
    t0 = pyramid.pop()
    t1 = pyramid.pop()
    pyramid.append([max(t0[i], t0[i + 1]) + t for i, t in enumerate(t1)])
# return pyramid[0][0]

# min max of rest of array
[min([a for a in array[i + 1:] if a > array[i]], default=-1)
 for i in range(len(array))]

# The zen of python
import this
