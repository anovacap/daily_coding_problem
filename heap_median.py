#!/usr/bin/python
# Heaps: 9.1 compute running median - Given a list of numbers return the median if the
# list as the list is iterated from left to right.

import heapq

def get_median(min_heap, max_heap):
    # min_heap, max_heap are lists
    if len(min_heap) > len(max_heap):
        print("min_heap = ", min_heap)
        return min_heap[0]
    elif len(min_heap) < len(max_heap):
        print("max_heap = ", max_heap)
        return -1 * max_heap[0]
    else:
        print("else trigger = ", (min_heap[0] + -1 * max_heap[0]) / 2.0 )
        return (min_heap[0] + -1 * max_heap[0]) / 2.0

def add(num, min_heap, max_heap):
    # if empty then add it to min heap.
    # calls get_median
    if len(min_heap) + len(max_heap) < 1:
        heapq.heappush(min_heap, num)
        return
    median = get_median(min_heap, max_heap)
    if num > median:
        heapq.heappush(min_heap, num)
    else:
        heapq.heappush(max_heap, -1 * num)

def rebalance(min_heap, max_heap):
    if len(min_heap) > len(max_heap)+ 1:
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -1 * root)
    elif len(max_heap) > len(min_heap) + 1:
        root = -1 * heapq.heappop(max_heap)
        heapq.heappush(min_heap, root)

def print_median(min_heap, max_heap):
    print(get_median(min_heap, max_heap))

def running_median(stream):
    # main program that calls add, rebalance and print_median
    # takes a list of integers
    min_heap = []
    max_heap = []
    for num in stream:
        add(num, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        print_median(min_heap, max_heap)

if __name__ == "__main__":
    s = [2,1,5,7,2,0,5]
    running_median(s)