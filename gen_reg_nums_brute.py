#!/usr/bin/python
# Heaps: 9.3 Generate Regular Numbers
# Regular number =  any number whose only prime divisor is 2, 3, or 5
# given an integer n, generate in order the first n regular numbers
# Brute Force Solution

def regular_numbers(n):
    # make lists of all the powers of 2,3, 5 up to n
    twos = [2 ** i for i in range(n)]
    print("twos = ", twos)
    threes = [3 ** i for i in range(n)]
    print("threes = ", threes)
    fives = [5 ** i for i in range(n)]
    print("fives = ", fives)
    solution = set()
    for two in twos:
        for three in threes:
            for five in fives:
                solution.add(two * three * five)
    l_sol = list(solution)
    print("L sol = ", l_sol[:n])
    return sorted(solution)[:n]

if __name__ == "__main__":
    a = 22
    print(regular_numbers(a))
