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

    # data = [2, 3, 1, 1, 4]
    data = [1, 1, 1000, 1, 1, 1, 1, 1, 1, 1]
    print(str(data))

    soln = [None]*len(data)
    N = len(data) - 1
    soln[N] = 0

    # start from second to last
    for i in range(N-1, -1, -1):
        if soln[i] is None:
            jmp = data[i]
            for j in range(jmp+1):
                if i+j > N:
                    continue

                if soln[i+j] is not None:
                    if soln[i] is None:
                        soln[i] = soln[i+j] + 1
                    else:
                        soln[i] = min(soln[i], soln[i+j]+1)

    print(soln)


if __name__ == '__main__':
    fire.Fire(run)

