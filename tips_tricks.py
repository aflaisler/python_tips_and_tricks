from __future__ import division
import pandas as pd
import numpy as np

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
