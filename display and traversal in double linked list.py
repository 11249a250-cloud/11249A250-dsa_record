AIM:
To create a doubly linked list and perform display and traversal operations by visiting each node sequentially in forward direction without using functions or modules.
program:
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = None

choice = 0

while choice != 3:
    print("1.Insert Node  2.Display Linked List  3.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        newnode = Node(data)
        if head is None:
            head = newnode
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp

    elif choice == 2:
        temp = head
        while temp is not None:
            print(temp.data)
            temp = temp.next

