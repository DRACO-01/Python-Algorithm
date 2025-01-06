
# Define the input array and target element
nums = [1, 43, 6, 7, 77, 4, 373, 9]
target = 373

# Step 1: Sort the array
# Binary search requires a (sorted array), so we sort the input array in ascending order.
nums.sort()

# Initialize the left and right pointers for the binary search
l = 0  # Starting index  of the array
r = len(nums) - 1  # too find the End of the array by -1

# Step 2: Perform binary search
# The while loop continues as long as there is a valid search space (l <= r).
while l <= r:
    # Calculate the mid index
    mid = (l + r) // 2  # Use floor division to avoid floating-point results
    
    # Check if the target is at the mid index
    if target == nums[mid]:
        # If the target is found, print its index and exit the loop
        print(mid, "is the index of the target element in the sorted array.")
        break
    
    # If the target is greater than the mid element, discard the left half
    elif target > nums[mid]:
        l = mid + 1  # Move the left pointer to mid + 1
    
    # If the target is smaller than the mid element, discard the right half
    elif target < nums[mid]:
        r = mid - 1  # Move the right pointer to mid - 1

# Step 3: Handle the case where the target is not found
# If the loop exits without finding the target, print a message indicating that the target was not found.
else:
    print("Target element not found.")