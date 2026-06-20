arr  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

length = len(arr)
while length > 0:
    if arr[length-1] % 2 == 0:
        arr.append(arr.pop(length-1))
        break
    length -= 1
print(arr)
