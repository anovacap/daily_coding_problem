#!/usr/bin/python
# input = list, n - list of numbers and a number to meet

def sum_is_n(ls, n):
    for i in ls:
        if n - i in ls:
            return True
    return False

if __name__ == "__main__":
    l = [10,15,3,7]
    k = 17
    print(sum_is_n(l,k))
