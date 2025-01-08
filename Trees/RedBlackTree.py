class Node:
    def __init__(self, key, color="red"):
        self.key = key  # Key of the node
        self.color = color  # Node color: "red" or "black"
        self.parent = None  # Parent node
        self.left = None  # Left child
        self.right = None  # Right child

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(key=None, color="black")  # Sentinel node for leaves
        self.root = self.TNULL  # Root of the tree

    def insert(self, key):
        # Create a new node
        new_node = Node(key)
        new_node.left = self.TNULL
        new_node.right = self.TNULL
        parent = None
        current = self.root

        # Traverse the tree to find the correct position
        while current != self.TNULL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        # Assign the parent to the new node
        new_node.parent = parent
        if not parent:
            self.root = new_node  # New node is root if parent is None
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix violations of red-black properties
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        # Fix red-black tree violations after insertion
        while node != self.root and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                # Parent is a left child
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    # Case 1: Uncle is red
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: Node is a right child
                        node = node.parent
                        self._rotate_left(node)
                    # Case 3: Node is a left child
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_right(node.parent.parent)
            else:
                # Parent is a right child
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    # Case 1: Uncle is red
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2: Node is a left child
                        node = node.parent
                        self._rotate_right(node)
                    # Case 3: Node is a right child
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_left(node.parent.parent)

        # Ensure the root is black
        self.root.color = "black"

    def _rotate_left(self, node):
        # Perform a left rotation around the given node
        temp = node.right
        node.right = temp.left
        if temp.left != self.TNULL:
            temp.left.parent = node
        temp.parent = node.parent
        if not node.parent:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp
        temp.left = node
        node.parent = temp

    def _rotate_right(self, node):
        # Perform a right rotation around the given node
        temp = node.left
        node.left = temp.right
        if temp.right != self.TNULL:
            temp.right.parent = node
        temp.parent = node.parent
        if not node.parent:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp
        temp.right = node
        node.parent = temp

    def inorder_traversal(self, node):
        # Perform an in-order traversal of the tree
        if node != self.TNULL:
            self.inorder_traversal(node.left)
            print(f"{node.key} ({node.color})", end=" ")
            self.inorder_traversal(node.right)

# Example usage
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    keys = [20, 15, 25, 10, 5, 1]
    for key in keys:
        rb_tree.insert(key)

    print("In-order traversal of the red-black tree:")
    rb_tree.inorder_traversal(rb_tree.root)
