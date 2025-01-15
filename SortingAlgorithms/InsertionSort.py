def insertion_sort(arr):
    """
    Function to perform Insertion Sort on a given list.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    None: The input list is sorted in place.
    """
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be positioned
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
