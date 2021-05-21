import fire
from typing import *

from dataclasses import dataclass, field
import numpy as np


def quicksort(A, l, r):
    if l < r:
        p = pivot(A, l, r)
        quicksort(A, l, p-1)
        quicksort(A, p+1, r)

def pivot(A, l, r):
    p = (l+r)//2
    print(p)

    while True:
        while A[l] < A[p]:
            l += 1
        while A[r] > A[p]:
            r -= 1
        if l >= r:
            return r
        print('l', l, A[l], 'r', r, A[r], 'p', p, A[p])

        tmp = A[l]
        A[l] = A[r]
        A[r] = tmp
        l += 1
        r -= 1

    return r


def run():
    A = [3, 5, 1, 2, 4, 9, 3, 3, 5, 2]

    print(A)
    quicksort(A, 0, len(A)-1)
    print(A)
    
    
if __name__ == '__main__':
    fire.Fire(run)

