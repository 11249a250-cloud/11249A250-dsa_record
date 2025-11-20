AIM
To delete nodes from the beginning, middle, and end of a singly linked list in Python by dynamically modifying node links without using functions or modules.
program:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

choice = 0

while choice != 4:
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

    elif choice == 2:
        if head is not None:
            head = head.next

    elif choice == 3:
        pos = int(input("Enter position: "))
        if head is not None:
            if pos == 1:
                head = head.next
            else:
                temp = head
                count = 1
                while temp is not None and count < pos - 1:
                    temp = temp.next
                    count += 1
                if temp is not None and temp.next is not None:
                    temp.next = temp.next.next

    elif choice == 4:
        if head is not None:
            if head.next is None:
                head = None
            else:
                temp = head
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None

    elif choice == 5:
        break
