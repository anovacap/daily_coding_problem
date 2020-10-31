#!/usr/bin/python
# Stacks and Queues 4.2 Balanced Brackets?
# return true or false

def balanced(s):
    stack = []
    for c in s:
        # check for openers and add to list - if not an opener move to else
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if not stack:
                # nothing in stack so closer starts return False
                return False
            if c == ')' and stack[-1] != '(' or \
               c == '}' and stack[-1] != '{' or \
               c == ']' and stack[-1] != '[':
                # match closers to last opener - first closer found will match last opner
                # this returns false if the match is not found
                return False
            # pop the last element from stack when closing match is found
            # when evrything is matched stack will be empty
            stack.pop()
    return len(stack) == 0 # or True

if __name__ == "__main__":
    e = "([])[]({})"
    f = "((}}[]"
    print(balanced(e))
    print(balanced(f))
