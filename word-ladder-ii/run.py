import fire
from typing import *

from dataclasses import dataclass, field
import numpy as np

import string


def get_next_words(beginWord, wordSet):
    # Find next nodes
    next_words = []
    for i in range(len(beginWord)):
        for c in string.ascii_lowercase:
            if c == beginWord[i]:
                continue
            new_word = beginWord[:i] + c + beginWord[i+1:]
            if new_word in wordSet:
                next_words.append(new_word)

    return next_words


def run():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    wordSet = set(wordList)

    seqs = []
    
    q = [[beginWord]]
    visited = set()
    longest_lvl = 0
    # Go level by level
    while len(q) > 0:
        seq = q.pop(0)
        print(seq)
        if len(seq) > longest_lvl:
            longest_lvl = len(seq)
            if len(seqs) > 0:
                break

        visited.add(seq[-1])

        candidates = get_next_words(seq[-1], wordSet)
        for c in candidates:
            if c in visited:
                continue
            if c == endWord:
                seqs.append(seq + [c])
            else:
                q.append(seq + [c])


    print('results')
    print('\n'.join([str(seq) for seq in seqs]))


if __name__ == '__main__':
    fire.Fire(run)
