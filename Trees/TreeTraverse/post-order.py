def postorder_traversal(self, node=None, result=None):
        """
        Postorder Traversal: Left -> Right -> Root
        """
        if node is None:
            node = self.root
        if result is None:
            result = []

        if node.left:
            self.postorder_traversal(node.left, result)
        if node.right:
            self.postorder_traversal(node.right, result)
        result.append(node.key)  # Visit the root

        return result