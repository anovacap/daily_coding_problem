#!/usr/bin/python
# ex 1.4 find the number of smaller elements to the right O(n2)
# for loop and sum (sum has a O(n) loop
def smaller_elm_right(arr):
	res = []
	for i, num in enumerate(arr):
		count = sum(val < num for val in arr[i + 1:])
		res.append(count)
	print("result = ", res)
	return res
if __name__ == "__main__":
	x = [6,7,2,8,9,1,4,12,5,10,3]
	j = smaller_elm_right(x)
	print(j)

