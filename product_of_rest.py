#!/usr/bin/env python
# ex. 1.1 Get product of all other elements in a list O(n)

def products(nums)
	prefix = []; suffix = []; result = []
	for num in nums:
		if prefix:
			prefix.append(prefix[-1] * num)
		else:
			prefix.append(num)
	print(prefix)
	for num in reversed(nums):
		if suffix:
			suffix.append(suffix[-1] * num)
		else:
			suffix.append(num)
	suffix = list(reversed(suffix))
	print(suffix)
	for i in range(len(nums)):
		if i == 0:
			result.append(suffix[i + 1])
		elif i == len(nums) - 1:
			result.append(prefix[i - 1])
		else:
			result.append(prefix[i - 1] * suffix[i + 1])
	print(result)
	return result
if __name__ == "__main__":
	x = [1,2,3,4,5]
	products(x)			
