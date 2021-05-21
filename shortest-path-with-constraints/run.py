import heapq
from collections import deque


nodes = [
    's',
    'pu1',
    'pu2',
    'pu3',
    'do1',
    'do2', 
    'do3', 
]

constraints = {
    'd01': 'pu1',
    'do2': 'pu2',
    'do3': 'pu3',
}

dq = [(0, 's')]


parents = {}
onpath = {}

while len(dq) > 0:
    # heapq implements a min-heap
    node = heapq.heappop(dq)

    for node in nodes:
        if node in constraints and constraints[node] not in onpath:
            continue
        



    


