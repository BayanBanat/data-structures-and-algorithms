class TNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BTree:
    def __init__(self):
        self.root = None
    
    def in_order(self):
        """
        Performs an in-order traversal on the binary tree and returns a list of node values.

        Returns:
            A list of node values in in-order traversal.
        """
        output=[]

        def _helper_in_order(root):
            if root.left:
                _helper_in_order(root.left)
            
            output.append(root.value)

            if root.right:
                _helper_in_order(root.right)
            
        _helper_in_order(self.root)
        return output

class BStTree(BTree):

    def tree_max(self):
       """
        This method performs an in-order traversal of the binary tree and finds the maximum value among all the nodes.
        It returns the maximum value found.

        input: None

        Returns:
        int: The maximum value in the binary tree.
       """
       values = self.in_order()
       max_value = 0
       for i in values:
           if i > max_value:
               max_value = i
       return max_value
               

if __name__ == "__main__":
    binary_tree=BStTree()
    binary_tree.root=TNode(2)
    binary_tree.root.left=TNode(7)
    binary_tree.root.right=TNode(5)
    binary_tree.root.left.left=TNode(2)
    binary_tree.root.left.right=TNode(6)
    binary_tree.root.left.right.right=TNode(11)
    binary_tree.root.right.right=TNode(9)
    binary_tree.root.right.right.left=TNode(4)
    print(binary_tree.in_order())
    print(binary_tree.tree_max())
    
  