AIM:
To traverse a singly linked list and display all its elements sequentially by visiting each node starting from the head node.
AIM:
class Node:
    def __init__(self, data):
        self.data = data
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

    elif choice == 2:
        temp = head
        while temp is not None:
            print(temp.data)
            temp = temp.next
