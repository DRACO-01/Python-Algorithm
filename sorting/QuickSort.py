def quick_sort(arr):
    """
    Function to perform Quick Sort on a given list.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: A new sorted list (Quick Sort is implemented recursively).
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Choose the first element as pivot
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
