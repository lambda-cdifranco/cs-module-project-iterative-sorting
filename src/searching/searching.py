def linear_search(arr, target):
    # Your code here
    for i, x in enumerate(arr):
        if x == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    # Your code here

    return -1  # not found


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, 6))

arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
print(linear_search(arr1, 6))