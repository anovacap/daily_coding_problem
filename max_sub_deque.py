#!/usr/bin/python
# Stacks and Queues 4.3 - Compute max subarray of length k
# dequeu method 

from collections import deque

def max_of_subarrays(l, k):
    q = deque()
    for i in range(k):
        while q and l[i] >= l[q[-1]]:
            q.pop()
        q.append(i)
    # loop invariant: q is a list of indecies where their corresponding values
    # are in descending order
    for i in range(k, len(l)):
        print(l[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and l[i] >= l[q[-1]]:
            q.pop()
        q.append(i)
    print(l[q[0]])
if __name__ == "__main__":
    l = [10,5,2,7,8,7]
    k = 3
    max_of_subarrays(l, k)
