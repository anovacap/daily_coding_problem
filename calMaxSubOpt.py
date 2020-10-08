#!/usr/bin/env python
# ex.1.3 optimized solution (Kandane's Algo) O(n)
def max_sub_sum(arr):
	max_ending = max_so_far = 0
	for i in arr:
		max_ending = max(i, max_ending + i)
		print("max_ending = ", max_ending)
		max_so_far = max(max_so_far, max_ending)
		print("max_so_far = ", max_so_far)
	return max_so_far
if __name__ == "__main__":
	x = [34,-50,42,14,-5,86]
	g = max_sub_sum(x)
	print(g)

