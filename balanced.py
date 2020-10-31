#!/usr/bin/python
# Stacks and Queues 4.2 Balanced Brackets?
# return true or false

def balanced(s):
    stack = []
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if not stack:
                return False
            if c == ')' and stack[-1] != '(' or \
               c == '}' and stack[-1] != '{' or \
               c == ']' and stack[-1] != '[':
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == "__main__":
    e = "([])[]({})"
    f = "((}}[]"
    print(balanced(e))
    print(balanced(f))
