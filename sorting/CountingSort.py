def counting_sort(arr):
    """
    Function to perform Counting Sort on a given list.
    
    Parameters:
    arr (list): The list of non-negative integers to be sorted.
    
    Returns:
    list: A sorted list.
    """
    if len(arr) == 0:
        return arr

    # Find the maximum value in the array
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Count the occurrences of each element
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i] * freq)

    return sorted_arr
