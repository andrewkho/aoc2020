import fire
from typing import *

from dataclasses import dataclass, field
import numpy as np


def run():
    # with open(fname, 'r') as f:
    #     lines = f.readlines()

    # data = [
    #     [int(x.strip()) for x in line.split(' ')]
    #     for line in lines
    # ]

    data = [-1, 0, 1, 2, -1, -4]
    print(str(data))

    # O(n^3) soln
    solns = set()
    N = len(data)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if data[i] + data[j] + data[k] == 0:
                    s = tuple(sorted([data[i], data[j], data[k]]))
                    if s not in solns:
                        solns.add(s)

    print(f'O(n^3): {solns}')

    # What if we sort the input first
    sorted_data = sorted(data)
    print(sorted_data)

    solns = []
    for i in range(N):
        if i > 0 and sorted_data[i] == sorted_data[i-1]:
            continue
        for j in range(i+1, N):
            if j != i+1 and sorted_data[j] == sorted_data[j-1]:
                continue
            for k in range(j+1, N):
                if k != j+1 and sorted_data[k] == sorted_data[k-1]:
                    continue
                if sorted_data[i] + sorted_data[j] + sorted_data[k] == 0:
                    solns.append((sorted_data[i], sorted_data[j], sorted_data[k]))

    print(f'O(n^3)-2: {solns}')

    # Hashmap solution
    solns = []
    sd = sorted(data)
    print(sd)

    # two_sum is order n
    def two_sum(arr, t) -> List[Tuple[int, int]]:
        hd = dict()
        for x in arr:  # O(n)
            if x not in hd:
                hd[x] = 1
            else:
                hd[x] += 1

        matches = []
        for x in arr:  # O(n)
            if hd[x] > 1:
                hd[x] -= 1
            else:
                del hd[x]

            if t-x in hd:
                matches.append((t-x, x))

        return matches
    
    for i in range(N):
        if i > 0 and sd[i] == sd[i-1]:
            continue

        v = sd[i]

        matches = two_sum(sd[i+1:], -v)
        for m in matches:
            solns.append((v, m[0], m[1]))

    print(f'O(n^2)-hashset: {solns}')

    # Two pointer solution
    solns = []
    sd = sorted(data)
    print(sd)
    
    N = len(sd)

    for i in range(N):
        if i == N-2:
            break
        if i > 0 and sd[i] == sd[i-1]:
            continue

        j = i+1
        k = N-1

        # March j forwards and k backwards until they meet
        while True:
            if j == k:
                break

            # Skip duplicates
            if j > i+1 and sd[j] == sd[j-1]:
                j+=1
                continue
            if k < N-1 and sd[k] == sd[k+1]:
                k -= 1
                continue

            if sd[i] + sd[j] + sd[k] > 0:
                k -= 1
            elif sd[i] + sd[j] + sd[k] < 0:
                j += 1
            else:
                solns.append((sd[i], sd[j], sd[k]))
                j += 1

    print(f'O(n^2)-two-pointer: {solns}')


if __name__ == '__main__':
    fire.Fire(run)

