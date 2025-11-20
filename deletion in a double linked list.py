AIM:
To delete nodes from the beginning, middle, and end of a doubly linked list by adjusting forward and backward links without using functions or modules.
program:
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = None

choice = 0

while choice != 5:
    print("1.Insert Node  2.Delete at Beginning  3.Delete at Middle  4.Delete at End  5.Exit")
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
        if head is not None:
            if head.next is not None:
                head = head.next
                head.prev = None
            else:
                head = None

    elif choice == 3:
        pos = int(input("Enter position: "))
        if head is not None:
            if pos == 1:
                if head.next is not None:
                    head = head.next
                    head.prev = None
                else:
                    head = None
            else:
                temp = head
                count = 1
                while temp is not None and count < pos:
                    temp = temp.next
                    count += 1
                if temp is not None:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next

    elif choice == 4:
        if head is not None:
            if head.next is None:
                head = None
            else:
                temp = head
                while temp.next is not None:
                    temp = temp.next
                temp.prev.next = None

