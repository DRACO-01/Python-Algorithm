def preorder_traversal(self, node=None, result=None):
        """
        Preorder Traversal: Root -> Left -> Right
        """
        if node is None:
            node = self.root
        if result is None:
            result = []

        result.append(node.key)  # Visit the root
        if node.left:
            self.preorder_traversal(node.left, result)
        if node.right:
            self.preorder_traversal(node.right, result)

        return result