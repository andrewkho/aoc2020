import fire
from typing import *

from dataclasses import dataclass, field
import numpy as np


def find_kth_2(la: list, al, lb: list, bl, k: int):
    print(f'la: {la}, lb: {lb}')
    print(f'al: {al}, bl: {bl}, k: {k}')

    if al >= len(la):
        return lb[bl+k]
    if bl >= len(lb):
        return la[al+k]
    if k == 0:
        return min(la[al], lb[bl])

    sa = min((k+1)//2-1, len(la)-1-al)
    sb = min((k+1)//2-1, len(lb)-1-bl)

    print(sa, sb)

    if la[al+sa] <= lb[bl+sb]:
        return find_kth_2(la, al+sa+1, lb, bl, k-sa-1)
    else:
        return find_kth_2(la, al, lb, bl+sb+1, k-sb-1)


def find_kth(la: list, al, lb: list, bl, k: int):

    print(f'la: {la}, lb: {lb}')
    print(f'al: {al}, bl: {bl}, k: {k}')

    # Stop conditions
    if al == len(la):
        return lb[bl+k]
    elif bl == len(lb):
        return la[al+k]
    elif k == 0:
        return min(la[al], lb[bl])

    # Check the k/2'th element from al
    sa = min((k+1)//2, len(la) - al)
    sb = min((k+1)//2, len(lb) - bl)

    va = la[al + sa - 1]
    vb = lb[bl + sb - 1]

    print(f'sa: {sa}, va: {va}, sb: {sb}, vb: {vb}')

    if va < vb:
        # we now only need to check elements in list a to the right of sa
        return find_kth(la, al + sa, lb, bl, k-sa)
    else:
        # and elements in list b to the left of sb
        return find_kth(la, al, lb, bl + sb, k-sb)

def getKth(array1, i, array2, x, k):
    if i == len(array1):
        return array2[x + k]
    elif x == len(array2):
        return array1[i + k]
    elif k == 0:
        return min(array1[i], array2[x])

    mid1 = min(len(array1) - i, (k + 1) // 2)
    mid2 = min(len(array2) - x, (k + 1) // 2)
    a = array1[i + mid1 - 1]
    b = array2[x + mid2 - 1]

    if a < b:
        return getKth(array1, i + mid1, array2, x, k - mid1)
    return getKth(array1, i, array2, x + mid2, k - mid2)


def run(fname: str):
    with open(fname, 'r') as f:
        lines = f.readlines()

    data = [
        [int(x.strip()) for x in line.split(' ')]
        for line in lines
    ]

    print(str(data))

    assert len(data) == 2

    if (len(data[0]) + len(data[1])) % 2 == 1:
        median_i = int((len(data[0]) + len(data[1]))/2)
        print(f"looking for index {median_i}") 
        val = find_kth_2(data[0], 0, data[1], 0, median_i)
        print(f"Found value {val}")
    else:
        median_l = int((len(data[0]) + len(data[1]))/2) - 1
        median_r = median_l + 1

        print(f"looking for index {median_l}") 
        vl = find_kth_2(data[0], 0, data[1], 0, median_l)
        print(f"Found value {vl}")
        print(f"looking for index {median_r}") 
        vr = find_kth_2(data[0], 0, data[1], 0, median_r)
        print(f"Found value {vr}")

        print(f'found median {(vl+vr)/2}')

    print(f'real median: {np.median(data[0] + data[1])}')
    


if __name__ == '__main__':
    fire.Fire(run)

