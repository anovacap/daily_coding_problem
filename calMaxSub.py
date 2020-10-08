#!/usr/bin/python
# ex. 1.3 brute force approach O(n3) slooowww
def max_subarray_sum(arr):
	current_max = 0
	for i in range(len(arr)):
		for j in range(i, len(arr) + 1):
			current_max = max(current_max, sum(arr[i:j]))
			print("current_max = ", current_max)
			print("sum arr[i:j] = ", sum(arr[i:j]))
	return current_max
if __name__=="__main__":
	x = [34,-50,42,14,-5,86]
	p = max_subarray_sum(x)
	print(p)

