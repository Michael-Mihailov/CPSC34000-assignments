def binarySearch(arr, target):
    length = len(arr)
    low = 0
    high = length - 1
    while (low <= high):
        mid = (low + high) // 2
        if int(arr[mid][0]) < target:
            low = mid + 1
        elif int(arr[mid][0]) > target:
            high = mid - 1
        else:
            return mid

    return -1