def bubble_sort(arr):
    """
    Function to perform Bubble Sort on a given list.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    None: The input list is sorted in place.
    """
    n = len(arr)  # Get the length of the list

    # Traverse through all array elements
    for i in range(n):
        # Initialize a flag to check if any swapping happened
        swapped = False

        # Last i elements are already sorted, so the inner loop can avoid them
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1.
            # If the element found is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark swapping as True

        # If no two elements were swapped in the inner loop, the list is already sorted
        if not swapped:
            break