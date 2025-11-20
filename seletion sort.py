AIM:
To sort a list of elements in ascending order using the Selection Sort algorithm by repeatedly selecting the minimum element from the unsorted portion and placing it at the correct position.
program:
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array:")
for i in range(n):
    print(arr[i])
