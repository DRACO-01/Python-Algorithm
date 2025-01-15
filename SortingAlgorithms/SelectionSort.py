def selection_sort(arr):
    """
    Function to perform Selection Sort on a given list.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    None: The input list is sorted in place.
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
