AIM
To create a singly linked list in Python and perform insertions at the beginning, middle, and end by creating nodes dynamically without using functions or modules.
program:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

choice = 0

while choice != 4:
    print("1.Insert at Beginning  2.Insert at Middle  3.Insert at End  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        newnode = Node(data)
        newnode.next = head
        head = newnode

    elif choice == 2:
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))
        newnode = Node(data)
        if pos == 1:
            newnode.next = head
            head = newnode
        else:
            temp = head
            count = 1
            while temp is not None and count < pos - 1:
                temp = temp.next
                count += 1
            if temp is not None:
                newnode.next = temp.next
                temp.next = newnode

    elif choice == 3:
        data = int(input("Enter data: "))
        newnode = Node(data)
        if head is None:
            head = newnode
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
