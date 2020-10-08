#!/usr/bin/env python
# ex. 1.3 Kandane's algo - max_sub_sum - sum(arr) - min_sub_sum - max of wrap or max_sub_sum O(n)
def wrapper(arr):
# get sum of arr - minus min_sub_sum(arr) return bigger of max_sub_sum and max_all
	max_all = sum(arr) - min_sub_sum(arr)
	return max(max_sub_sum(arr), max_all)
def max_sub_sum(arr):
# calc max subarray sum 
	max_ending = max_so_far = 0
	for i in arr:
		max_ending = max(i, max_ending + i)
#		print("max_ending = ", max_ending)
		max_so_far = max(max_so_far, max_ending)
		print("max_so_far = ", max_so_far)
	return max_so_far
def min_sub_sum(arr):
#cal min subarray sum
	min_ending_here = min_so_far = 0
	for i in arr:
		min_ending_here = min(i, min_ending_here + i)
		min_so_far = min(min_so_far, min_ending_here)
	print("min_so_far = ", min_so_far)
	return min_so_far
if __name__ == "__main__":
	x = [34,-50,42,14,-5,86]
	g = wrapper(x)
	print(g)

