AIM:
To sort a list of elements in ascending order using Quick Sort by repeatedly partitioning the array around a pivot element and arranging smaller elements before the pivot and larger elements after it.
program:
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input()))

stack = [(0, n-1)]

while stack:
    low, high = stack.pop()
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        p = i + 1
        stack.append((low, p-1))
        stack.append((p+1, high))

print("Sorted array:")
for i in range(n):
    print(arr[i])
