import fire
from typing import *
import string

from dataclasses import dataclass, field
import numpy as np


@dataclass
class Node:
    word: Optional[str]
    children: Dict[str, 'Node'] = field(default_factory=lambda: dict())


def build_trie(words):
    trie = Node(None)

    for w in words:
        if len(w) == 0:
            continue
        curr_node = trie
        for c in w:
            if c not in curr_node.children:
                curr_node.children[c] = Node(None)

            curr_node = curr_node.children[c] 

        assert curr_node.word is None, (w, curr_node.word)

        curr_node.word = w

    return trie


def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return False

    return True   


def run():
    #words = ["bat", "tab", "cat"]
    #words = ["abcd", "dcba", "lls", "s", "sssll"]
    words = ["a", ""]

    print(words)
    
    trie = build_trie(words)

    print(trie)

    pairs = []

    for w in words:
        # Use the trie to find reverse matching
        curr_node = trie
        print(w)
        for i in range(len(w)-1, -1, -1):
            if curr_node.word is not None:
                # Potential match so long as rest of this word is palindrome
                if is_palindrome(w[0:i]):
                    pairs.append(curr_node.word + w)

            c = w[i]
            if c not in curr_node.children:
                break
            else:
                curr_node = curr_node.children[c]

        if i <= 0:
            if curr_node.word is not None and w != curr_node.word:
                pairs.append(curr_node.word + w)

    print(pairs)


if __name__ == '__main__':
    fire.Fire(run)

