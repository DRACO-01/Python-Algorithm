def merge(left, right):
    # Merges two sorted arrays into a single sorted array
    sorted_array = []
    i = j = 0

    # Compare elements and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append remaining elements from left and right
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


def merge_sort(arr):
    # Base case: array with one or no elements is already sorted
    if len(arr) <= 1:
        return arr

    # Split array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Merge Sorted Array:", sorted_arr)
