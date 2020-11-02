#!/usr/bin/python
# Stacks and Queues 4.4 - Reconstruct array using +/- signs
# Function recieves a list of + and minuses returns a list of numbers
# [None, '+','+', '-', '+'] == [0,1,3,2,4] 

def plus_minus(arr):
    res = []
    for i in range(len(arr)):
        if arr[i] == '+' or arr[i] == None:
            res.append(i)
        else:
            res.insert((i-1), i)
    return res

if __name__ == "__main__":
    inp = ['+','+', '+', '-','+']
    print(plus_minus(inp))
