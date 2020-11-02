#!/usr/bin/python
# Stacks and Queues 4.4 - Reconstruct array using +/- signs
# Function recieves a list of + and minuses returns a list of numbers
# [None, '+','+', '-', '+'] == [0,1,3,2,4] 

def recon(arr):
    res = []
    stack = []
    for i in range(len(arr) - 1):
        if arr[1+1] == '-':
            stack.append(i)
        else:
            res.append(i)
            while stack:
                res.append(stack.pop())
    stack.append(len(arr) - 1)
    while stack:
        res.append(stack.pop())
    return res
if __name__ == "__main__":
    inp = ['+','+', '+', '-','+']
    print(recon(inp))