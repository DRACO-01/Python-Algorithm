def exponential_search(arr, target):
    if len(arr) == 0:
        return -1

    # If the target is at the first position
    if arr[0] == target:
        return 0

    # Find the range to do binary search
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    # Perform binary search on the found range
    return binary_search_iterative(arr, target, i // 2, min(i, len(arr)-1))

def binary_search_iterative(arr, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Usage
sorted_nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
index = exponential_search(sorted_nums, 15)
print(index)  # Output: 7
