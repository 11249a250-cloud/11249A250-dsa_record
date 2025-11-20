AIM:
To implement a simple hash table using an array with a hash function and linear probing for inserting, searching, and deleting elements without using functions or modules.
program:
size = int(input("Enter size of hash table: "))
hash_table = [None] * size

choice = 0

while choice != 4:
    print("1.Insert  2.Search  3.Delete  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        index = key % size
        start = index
        while hash_table[index] is not None:
            index = (index + 1) % size
            if index == start:
                break
        if hash_table[index] is None:
            hash_table[index] = key
        else:
            print("Hash Table Full")

    elif choice == 2:
        key = int(input("Enter key to search: "))
        index = key % size
        start = index
        found = False
        while hash_table[index] is not None:
            if hash_table[index] == key:
                found = True
                break
            index = (index + 1) % size
            if index == start:
                break
        if found:
            print("Key found at index", index)
        else:
            print("Key not found")

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        index = key % size
        start = index
        found = False
        while hash_table[index] is not None:
            if hash_table[index] == key:
                hash_table[index] = None
                found = True
                break
            index = (index + 1) % size
            if index == start:
                break
        if found:
            print("Key deleted")
        else:
            print("Key not found")
