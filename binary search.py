AIM:
To search an element in a sorted list by repeatedly dividing the search range into halves to locate the element efficiently.
program:
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input()))
key = int(input("Enter element to search: "))
low = 0
high = n - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element found at position:", mid)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print("Element not found")
