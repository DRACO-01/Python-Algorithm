class Node:
    def __init__(self, key):
        # Each node has a key, and pointers to left and right children
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        # Initialize the tree with no root
        self.root = None

    def insert(self, key):
        # Insert a new key into the binary tree
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.key:
            # If the key is smaller, go to the left subtree
            if current.left:
                self._insert_recursive(current.left, key)
            else:
                current.left = Node(key)
        else:
            # If the key is larger, go to the right subtree
            if current.right:
                self._insert_recursive(current.right, key)
            else:
                current.right = Node(key)

    def inorder_traversal(self, node=None, result=None):
        # Perform an inorder traversal (Left, Root, Right)
        if node is None:
            node = self.root
        if result is None:
            result = []

        if node.left:
            self.inorder_traversal(node.left, result)
        result.append(node.key)
        if node.right:
            self.inorder_traversal(node.right, result)

        return result


# Example usage:
bt = BinaryTree()
keys = [50, 30, 70, 20, 40, 60, 80]
for key in keys:
    bt.insert(key)

print("Inorder Traversal of Tree:", bt.inorder_traversal())
