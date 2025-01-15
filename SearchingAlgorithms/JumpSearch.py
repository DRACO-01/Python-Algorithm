import math
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Jump size

    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search in the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Usage
sorted_nums = [1, 3, 5, 7, 9, 11, 13]
index = jump_search(sorted_nums, 9)
print(index)  # Output: 4
