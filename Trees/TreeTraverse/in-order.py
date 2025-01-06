def inorder_traversal(self, node=None, result=None):
        """
        Inorder Traversal: Left -> Root -> Right
        """
        if node is None:
            node = self.root
        if result is None:
            result = []

        if node.left:
            self.inorder_traversal(node.left, result)
        result.append(node.key)  # Visit the root
        if node.right:
            self.inorder_traversal(node.right, result)

        return result