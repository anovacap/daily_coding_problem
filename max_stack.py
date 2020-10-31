#!/usr/bin/python
# Stacks and Queues 4.1; Implementing a Max Stack


class stack:
    def __init__(self):
        self.stack = []
        self.maxes = []

    def _push(self, data):
        self.stack.append(data)
        if self.maxes:
            self.maxes.append(max(data, self.maxes[-1]))
        else:
            self.maxes.append(data)
    def _pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def _max(self):
        return self.maxes[-1]


if __name__ == "__main__":
    s = stack()
    s._push(5)
    s._push(4)
    s._push(3)
    s._push(2)
    s._push(1)
    print(s.stack)
    print(s._max())


    