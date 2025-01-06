class Node:
    """
    Represents a single node in the AVL Tree.
    Each node contains:
    - key: The value stored in the node.
    - height: Height of the node.
    - left: Pointer to the left child.
    - right: Pointer to the right child.
    """
    def __init__(self, key):
        self.key = key
        self.height = 1  # A new node starts with height 1
        self.left = None
        self.right = None


class AVLTree:
    """
    Implementation of an AVL Tree with insertion and balancing.
    """
    def get_height(self, node):
        """
        Returns the height of the node.
        :param node: The node whose height is required.
        :return: Height of the node, or 0 if node is None.
        """
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """
        Returns the balance factor of the node.
        :param node: The node whose balance factor is required.
        :return: Balance factor (height of left - height of right).
        """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        """
        Performs a right rotation on the subtree rooted at y.
        :param y: The root of the subtree to rotate.
        :return: New root of the subtree.
        """
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x):
        """
        Performs a left rotation on the subtree rooted at x.
        :param x: The root of the subtree to rotate.
        :return: New root of the subtree.
        """
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, node, key):
        """
        Inserts a key into the AVL tree and rebalances the tree if needed.
        :param node: The root of the subtree where the key will be inserted.
        :param key: The value to insert.
        :return: The new root of the subtree.
        """
        # Perform normal BST insertion
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            # Duplicate keys are not allowed in AVL Tree
            return node

        # Update height of this ancestor node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Get the balance factor of this ancestor node
        balance = self.get_balance(node)

        # Rebalance the node if it's unbalanced
        # Case 1: Left Left
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Case 2: Right Right
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Case 3: Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Case 4: Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def inorder_traversal(self, node, result=None):
        """
        Performs an in-order traversal of the tree.
        :param node: The root of the subtree to traverse.
        :param result: A list to store traversal result.
        :return: The in-order traversal result.
        """
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.key)
            self.inorder_traversal(node.right, result)
        return result


# Example usage
avl = AVLTree()
root = None

# Insert elements
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = avl.insert(root, key)

# In-order traversal of the AVL tree
print("In-order Traversal of AVL Tree:", avl.inorder_traversal(root))
