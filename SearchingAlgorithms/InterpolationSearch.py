def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Avoid division by zero
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            else:
                return -1

        # Interpolation formula
        pos = low + int((float(target - arr[low]) / (arr[high] - arr[low])) * (high - low))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Usage
sorted_nums = [10, 20, 30, 40, 50, 60, 70]
index = interpolation_search(sorted_nums, 50)
print(index)  # Output: 4
