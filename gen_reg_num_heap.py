#!/usr/bin/python
# Heap 9.3 Generate regular numbers
# Heapq version

import heapq

def regular_nums(n):
    solution = [1]
    last = 0
    count = 0
    while count < n:
        x = heapq.heappop(solution)
        if x > last:
            yield x
            last = x
            count += 1
            heapq.heappush(solution, 2 * x)
            heapq.heappush(solution, 3 * x)
            heapq.heappush(solution, 5 * x)
    return solution

if __name__=="__main__":
    a = 22
    x = [i for i in regular_nums(a)]
    print(x)
