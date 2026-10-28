def linearSearch(arr, target):
    length = len(arr)
    for i in range(length):
        if int(arr[i][0]) == target:
            return i

    return -1