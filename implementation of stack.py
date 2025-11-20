AIM
To implement a stack using a list in Python by performing push, pop, and display operations based on user choice.
program:
stack = []
top = -1
size = int(input("Enter stack size: "))

while True:
    print("1.Push  2.Pop  3.Display  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        if top == size - 1:
            print("Stack Overflow")
        else:
            val = int(input("Enter value to push: "))
            stack.append(val)
            top += 1
    elif ch == 2:
        if top == -1:
            print("Stack Underflow")
        else:
            print("Popped element:", stack[top])
            stack.pop()
            top -= 1
    elif ch == 3:
        if top == -1:
            print("Stack is Empty")
        else:
            print("Stack elements:")
            for i in range(top, -1, -1):
                print(stack[i])
    elif ch == 4:
        break
    else:
        print("Invalid Choice")
