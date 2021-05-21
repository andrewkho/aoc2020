import fire
from typing import *

from dataclasses import dataclass, field
import numpy as np


def get_spiral(data, up, dn, lf, rt):
    if up >= dn or lf >= rt:
        return []

    result = []
    for j in range(lf, rt):
        result.append(data[up, j])
    for i in range(up+1, dn):
        result.append(data[i, rt-1])
    for j in range(rt-2, lf-1, -1):
        result.append(data[dn-1, j])
    for i in range(dn-2, up, -1):
        result.append(data[i, lf])

    print(result)
    result.extend(get_spiral(data, up+1, dn-1, lf+1, rt-1))

    return result


def run():

    
    # with open(fname, 'r') as f:
    #     lines = f.readlines()

    # data = [
    #     [int(x.strip()) for x in line.split(' ')]
    #     for line in lines
    # ]

    data = np.array([
        [1, 2, 3, 1.5],
        [4, 5, 6, 2.5],
        [7, 8, 9, 3.5]
    ])

    print(str(data))


    print(get_spiral(data, up=0, dn=data.shape[0], lf=0, rt=data.shape[1]))



if __name__ == '__main__':
    fire.Fire(run)

