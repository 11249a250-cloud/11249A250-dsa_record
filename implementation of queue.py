AIM:
To implement a queue using a list in Python by performing enqueue, dequeue, and display operations based on user choice following FIFO (First In First Out) order.
program:
queue = []
front = -1
rear = -1
size = int(input("Enter queue size: "))

while True:
    print("1.Enqueue  2.Dequeue  3.Display  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        if rear == size - 1:
            print("Queue Overflow")
        else:
            val = int(input("Enter value to enqueue: "))
            if front == -1:
                front = 0
            rear += 1
            queue.append(val)

    elif ch == 2:
        if front == -1 or front > rear:
            print("Queue Underflow")
        else:
            print("Dequeued element:", queue[front])
            front += 1

    elif ch == 3:
        if front == -1 or front > rear:
            print("Queue is Empty")
        else:
            print("Queue elements:")
            for i in range(front, rear + 1):
                print(queue[i])

    elif ch == 4:
        break

    else:
        print("Invalid Choice")
