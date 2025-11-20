AIM:
To implement insertion operations at the beginning, middle, and end in a doubly linked list by dynamically creating nodes and adjusting forward and backward links.
program:
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = None

choice = 0

while choice != 4:
    print("1.Insert at Beginning  2.Insert at Middle  3.Insert at End  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        newnode = Node(data)
        if head is None:
            head = newnode
        else:
            newnode.next = head
            head.prev = newnode
            head = newnode

    elif choice == 2:
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))
        newnode = Node(data)
        if pos == 1:
            if head is None:
                head = newnode
            else:
                newnode.next = head
                head.prev = newnode
                head = newnode
        else:
            temp = head
            count = 1
            while temp is not None and count < pos - 1:
                temp = temp.next
                count += 1
            if temp is not None:
                newnode.next = temp.next
                newnode.prev = temp
                if temp.next is not None:
                    temp.next.prev = newnode
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
            newnode.prev = temp
