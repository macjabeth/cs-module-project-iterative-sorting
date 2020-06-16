# O(n) runtime | O(1) space
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        value = arr[middle]
        if value == target:
            return middle
        elif target < value:
            right = middle - 1
        else:
            left = middle + 1
    return -1  # not found
