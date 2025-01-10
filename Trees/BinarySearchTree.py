# lesser than the root value stores in the left side of the of the tree 
# greater than the root valeu stores in the right side of the tree

# binary search tree BST

class BSTnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def Add(self,data):
        if not self.root:
            self.root = BSTnode(data)
            return
        self.recursiveadd(data,self.root)

    def recursiveadd(self,data,node):
        if data <node.data:
            if not node.left:
                node.left = BSTnode(data)
            else:
                self.recursiveadd(data,node.left)
        elif data > node.data:
            if not node.right:
                node.right = BSTnode(data)
            else:
                self.recursiveadd(data,node.right)


    def remove(self,data):
        if self.root is None:
            print("tree is empty")
            return
        if self.root.data==data:
            self.root = None
            return
        self.recursiveremove(self.root,data)

    def recursiveremove(self,node,data):
        if node.left and node.left.data==data:
            node.left = None
        elif node.right and node.right.data == data:
            node.right = None
        elif data < node.data:
            self.recursiveremove(node.left,data)
        elif data > node.right:
            self.recursiveremove(node.right,data)                         
    



        
bst1 = BinarySearchTree()
# lesser than the root value stores in the left side of the of the tree 
# greater than the root valeu stores in the right side of the tree

# binary search tree BST

class BSTnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def Add(self,data):
        if not self.root:
            self.root = BSTnode(data)
            return
        self.recursiveadd(data,self.root)

    def recursiveadd(self,data,node):
        if data <node.data:
            if not node.left:
                node.left = BSTnode(data)
            else:
                self.recursiveadd(data,node.left)
        elif data > node.data:
            if not node.right:
                node.right = BSTnode(data)
            else:
                self.recursiveadd(data,node.right)


    def remove(self,data):
        if self.root is None:
            print("tree is empty")
            return
        if self.root.data==data:
            self.root = None
            return
        self.recursiveremove(self.root,data)

    def recursiveremove(self,node,data):
        if node.left and node.left.data==data:
            node.left = None
        elif node.right and node.right.data == data:
            node.right = None
        elif data < node.data:
            self.recursiveremove(node.left,data)
        elif data > node.right:
            self.recursiveremove(node.right,data)                         
    



        
bst1 = BinarySearchTree()
bst1.Add(10)
bst1.Add(5)
bst1.Add(60)
bst1.Add(90)
