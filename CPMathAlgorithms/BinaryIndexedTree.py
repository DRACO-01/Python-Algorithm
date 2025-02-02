class BinaryIndexedTree:
    def __init__(self, size):
        """Initializes an empty Binary Indexed Tree with given size."""
        self.size = size
        self.tree = [0] * (size + 1)  # 1-indexed array

    def update(self, index, value):
        """
        Increases the value at position `index` (0-indexed) by `value`.
        Complexity: O(log(n))
        """
        # BIT is 1-indexed
        index += 1
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def prefix_sum(self, index):
        """
        Computes the prefix sum of elements up to and including `index` (0-indexed).
        Complexity: O(log(n))
        """
        result = 0
        index += 1  # Convert to 1-indexed
        while index:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_sum(self, left, right):
        """
        Returns the sum of elements in the interval [left, right] (0-indexed).
        """
        return self.prefix_sum(right) - (self.prefix_sum(left - 1) if left > 0 else 0)


# Example usage:
if __name__ == "__main__":
    arr = [1, 7, 3, 0, 7, 8, 3, 2, 6, 2]
    n = len(arr)
    bit = BinaryIndexedTree(n)
    for i, num in enumerate(arr):
        bit.update(i, num)
    print("Prefix sum up to index 5:", bit.prefix_sum(5))
    print("Range sum between index 3 and 8:", bit.range_sum(3, 8))
