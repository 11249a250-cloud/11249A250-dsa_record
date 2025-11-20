AIM:
To sort a list of elements in ascending order using Merge Sort by repeatedly dividing the array into halves, sorting each half, and merging them into a sorted array.
program:
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input()))

size = 1
while size < n:
    left = 0
    while left + size < n:
        mid = left + size - 1
        right = min(left + 2*size - 1, n - 1)
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        for k in range(len(temp)):
            arr[left + k] = temp[k]
        left += 2*size
    size *= 2

print("Sorted array:")
for i in range(n):
    print(arr[i])
