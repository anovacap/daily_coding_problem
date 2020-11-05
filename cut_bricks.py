#!/usr/bin/python
# Hash Tables 5.1 - Cut brick wall 
# Given a list of lists of numbers that add up to the sam number find the
# index has the fewest cuts from top to bottom.
# defaultdict (alows for a keys to be entered later - no key error - a default value is created for keys that 
# don't exist)
# 
from collections import defaultdict

def cut_bricks(ls):
    cuts = defaultdict(int)
    for i in ls:
        length = 0 
        for j in i[:-1]:
            length += j
            cuts[length] += 1
    return len(ls) - max(cuts.values())

if __name__ == "__main__":
    w = [[3,5,1,1],[2,3,3,2],[5,5],[4,4,2],[1,3,3,3,],[1,1,6,1,1]]
    print(cut_bricks(w))
