AIM:
To use a stack to check whether a given expression contains balanced parentheses by pushing opening brackets onto the stack and popping them when matching closing brackets appear.
program:
expr = input("Enter expression: ")
stack = []
top = -1
balanced = True
for ch in expr:
    if ch == '(' or ch == '{' or ch == '[':
        stack.append(ch)
        top += 1
    elif ch == ')' or ch == '}' or ch == ']':
        if top == -1:
            balanced = False
            break
        c = stack[top]
        stack.pop()
        top -= 1
        if (ch == ')' and c != '(') or (ch == '}' and c != '{') or (ch == ']' and c != '['):
            balanced = False
            break
if top != -1:
    balanced = False
if balanced:
    print("Balanced")
else:
    print("Not Balanced")
