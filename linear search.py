AIM:
To search an element in a list by checking each element sequentially until the required element is found.
program:
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input()))
key = int(input("Enter element to search: "))
found = False
for i in range(n):
    if arr[i] == key:
        print("Element found at position:", i)
        found = True
        break
if not found:
    print("Element not found")
