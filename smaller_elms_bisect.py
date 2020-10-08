#!/usr/bin/python
import bisect
# bisect - support for maintaining a list in sorted order without having to sort the list after each insertion. Called bisect because it uses a basic bisection algorithm to do its work.
# bisect.bisect_left() returns the index of the sort where the number is placed to the left.
# bisect.insort() returns the sorted list that it is given (seen is sorted and updated.
def smaller_counts(lst):
	result = []
	seen = []
	for num in reversed(lst):
		i = bisect.bisect_left(seen, num)
		result.append(i)
		bisect.insort(seen, num)
		print(seen)
	return list(reversed(result))

if __name__ == "__main__":
	l = [3,4,9,6,1]
	g = smaller_counts(l)
	print(g)
