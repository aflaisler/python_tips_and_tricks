import pandas as pd
import numpy as np
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from collections import deque
from itertools import product

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


# graphs breadth_first_traversal
import networkx as nx
g_adj = {
    0: {1, 4},
    1: {0, 2, 3},
    2: {1, 3, 5},
    3: {1, 2, 4},
    4: {0, 3, 4},
    5: {2}}
G = nx.from_dict_of_lists(g_adj)  # example graph


def breadth_first_traversal(G, initial_node=0):
    Q = deque([initial_node])
    # Using a list so I can preserve the order I visited nodes.
    visited = []

    while Q:
        node = Q.popleft()
        if node not in visited:
            visited.append(node)
            Q.extend(G.neighbors(node))
    return visited


def depth_first_traversal(G, initial_node=0):
    S = deque([initial_node])
    visited = []
    while S:
        node = S.pop()
        if node not in visited:
            visited.append(node)
            S.extend(reversed(G.neighbors(node)))
    return visited
