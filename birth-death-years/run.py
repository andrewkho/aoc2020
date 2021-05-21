import fire
from typing import *

from dataclasses import dataclass, field
import numpy as np



def run():
    data = [
        (1901, 2020),
        (1948, 1949),
        (1980, 1990),
        (1939, 2000)
    ]

    print(data)

    # Find the year with most people alive
    # We can e.g. put birth/death years into a hash map, iterate through sorted keys and tally

    hm = dict()
    for by, dy in data:
        if by not in hm:
            hm[by] = [0, 0]
        hm[by][0] += 1

        if dy not in hm:
            hm[dy] = [0, 0]
        hm[dy][1] += 1
            
    alive = 0
    max_alive = 0
    max_alive_yr = 0
    for yr in sorted(hm.keys()):
        alive += hm[yr][0]
        if alive > max_alive:
            max_alive = alive
            max_alive_yr = yr
        alive -= hm[yr][1]
    
    print(hm, max_alive, max_alive_yr)

    
    
if __name__ == '__main__':
    fire.Fire(run)

