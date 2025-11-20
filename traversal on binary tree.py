AIM:
To create a binary tree and perform traversal operations such as inorder, preorder, and postorder by visiting nodes in their respective sequences without using functions or modules.
program:
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = None

choice = 0

while choice != 5:
    print("1.Insert Node  2.Inorder Traversal  3.Preorder Traversal  4.Postorder Traversal  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        newnode = Node(data)
        if root is None:
            root = newnode
        else:
            temp = root
            while True:
                if data < temp.data:
                    if temp.left is None:
                        temp.left = newnode
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = newnode
                        break
                    else:
                        temp = temp.right

    elif choice == 2:
        stack = []
        temp = root
        while True:
            if temp is not None:
                stack.append(temp)
                temp = temp.left
            elif stack:
                temp = stack.pop()
                print(temp.data)
                temp = temp.right
            else:
                break

    elif choice == 3:
        stack = []
        temp = root
        while stack or temp is not None:
            if temp is not None:
                print(temp.data)
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                temp = temp.right

    elif choice == 4:
        stack = []
        last = None
        temp = root
        while stack or temp is not None:
            if temp is not None:
                stack.append(temp)
                temp = temp.left
            else:
                peek = stack[-1]
                if peek.right is not None and last != peek.right:
                    temp = peek.right
                else:
                    print(peek.data)
                    last = peek
                    stack.pop()
