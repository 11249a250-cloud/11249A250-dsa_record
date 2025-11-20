AIM:
To sort a list of elements in ascending order using Heap Sort by building a max-heap and repeatedly extracting the maximum element to achieve a sorted array.
program:
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input()))

i = n // 2 - 1
while i >= 0:
    j = i
    while j < n:
        largest = j
        l = 2 * j + 1
        r = 2 * j + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != j:
            arr[j], arr[largest] = arr[largest], arr[j]
            j = largest
        else:
            break
    i -= 1

i = n - 1
while i > 0:
    arr[0], arr[i] = arr[i], arr[0]
    j = 0
    while j < i:
        largest = j
        l = 2 * j + 1
        r = 2 * j + 2
        if l < i and arr[l] > arr[largest]:
            largest = l
        if r < i and arr[r] > arr[largest]:
            largest = r
        if largest != j:
            arr[j], arr[largest] = arr[largest], arr[j]
            j = largest
        else:
            break
    i -= 1

print("Sorted array:")
for i in range(n):
    print(arr[i])
