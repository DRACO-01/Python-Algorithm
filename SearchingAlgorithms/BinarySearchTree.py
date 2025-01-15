class Node:
    """
    Class to represent a node in a Binary Search Tree.
    Each node contains a value and references to its left and right children.
    """
    def __init__(self, value):
        self.value = value  # The value of the node
        self.left = None    # Left child (smaller values)
        self.right = None   # Right child (larger values)


class BinarySearchTree:
    """
    Class to represent a Binary Search Tree.
    It supports insertion, searching, and traversal operations.
    """
    def __init__(self):
        self.root = None  # The root node of the BST

    def insert(self, value):
        """
        Insert a value into the BST. If the tree is empty, 
        the value becomes the root. Otherwise, it is placed
        in the correct position following BST rules.
        """
        if self.root is None:
            self.root = Node(value)  # The first value becomes the root
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        """
        Helper method to recursively insert a value into the BST.
        It compares the value with the current node's value and
        places it in the left or right subtree accordingly.
        """
        if value < node.value:  # Smaller values go to the left
            if node.left is None:
                node.left = Node(value)  # Create a new node if left is empty
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:  # Larger values go to the right
            if node.right is None:
                node.right = Node(value)  # Create a new node if right is empty
            else:
                self._insert_recursively(node.right, value)

    def search(self, value):
        """
        Search for a value in the BST. Returns True if found, otherwise False.
        """
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        """
        Helper method to recursively search for a value in the BST.
        If the value matches the current node, it returns True.
        """
        if node is None:
            return False  # Base case: value not found
        if value == node.value:
            return True  # Value found
        elif value < node.value:
            return self._search_recursively(node.left, value)  # Search left
        else:
            return self._search_recursively(node.right, value)  # Search right

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the BST (Left, Root, Right).
        Returns a list of values in ascending order.
        """
        result = []
        self._inorder_traversal_recursively(self.root, result)
        return result

    def _inorder_traversal_recursively(self, node, result):
        """
        Helper method to recursively perform an inorder traversal.
        Appends the values to the result list in sorted order.
        """
        if node is not None:
            self._inorder_traversal_recursively(node.left, result)  # Traverse left
            result.append(node.value)  # Visit the root
            self._inorder_traversal_recursively(node.right, result)  # Traverse right


# Example usage:
bst = BinarySearchTree()
bst.insert(50)  # Insert value 50
bst.insert(30)  # Insert value 30
bst.insert(70)  # Insert value 70
bst.insert(20)  # Insert value 20
bst.insert(40)  # Insert value 40
bst.insert(60)  # Insert value 60
bst.insert(80)  # Insert value 80

print("Inorder Traversal:", bst.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 70, 80]
print("Search for 40:", bst.search(40))  # Output: True
print("Search for 100:", bst.search(100))  # Output: False
