def counting_sort(arr, exp):
    # Initialize a count array to store counts of digits
    n = len(arr)
    count = [0] * 10
    output = [0] * n

    # Count occurrences of each digit in the current place value (exp)
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count[i] to contain actual positions of the digits in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array by placing elements in their correct position
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the sorted values back to arr
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)

    # Perform counting sort for each digit (units, tens, hundreds, ...)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Radix Sorted Array:", arr)
