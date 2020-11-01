#!/usr/bin/python
# Stacks and Queues 4.3 - Compute maximum of k length subarrays
# Given a list of integers and an integer(k) find the max integer in the length of k
# return a list of the max integers in the subarray.
# Make a window len(k) and move it, checking the max watch out for off by ones
def max_subarray(arr, k):
    res = []
    for i in range(len(arr) - k + 1):
        res.append(max(arr[i:i+k]))
    return res

if __name__ == "__main__":
    a = [10,5,2,7,8,7]
    n = 3
    print(max_subarray(a,n))

