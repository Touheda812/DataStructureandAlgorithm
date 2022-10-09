arr = [-2, 3, 4, 7, 8, 9, 11, 13]
target = 11


# search(arr,target)

def search(arr, target):
    left = 0
    right = arr.length - 1
    while left <= right:
        mid = (left + right) / 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
