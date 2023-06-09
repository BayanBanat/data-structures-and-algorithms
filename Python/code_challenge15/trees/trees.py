class TreeNode:
    """
        Represents a node in a binary tree.

        Args:
            value: The value stored in the node.
        """
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
        Represents a binary tree.

        The tree is initially empty, with no root node.
        """
    def __init__(self):
        self.root = None
    
    def pre_order(self):
        """
        Performs a pre-order traversal on the binary tree and returns a list of node values.

        Returns:
            A list of node values in pre-order traversal.
        """
        output=[]
        
        def _helper_pre_order(root):
            output.append(root.value)
            if root.left:
                _helper_pre_order(root.left)
            if root.right:
                _helper_pre_order(root.right)
           
        
        _helper_pre_order(self.root)
        return output
    

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
    
    def post_order(self):
        """
        Performs a post-order traversal on the binary tree and returns a list of node values.

        Returns:
            A list of node values in post-order traversal.
        """
        output=[]

        def _helper_in_order(root):
            if root.left:
                _helper_in_order(root.left)
            
            if root.right:
                _helper_in_order(root.right)

            output.append(root.value)

            
        _helper_in_order(self.root)
        return output


class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Adds a new node with the given value in the correct location in the binary search tree.

        Args:
            value: The value to be added.
        """
        new_node = TreeNode(value)

        def _add_helper(node, new_node):
            if new_node.value > node.value:
                if node.right is None:
                    node.right = new_node
                else:
                    _add_helper(node.right, new_node)
            else:
                if node.left is None:
                    node.left = new_node
                else:
                    _add_helper(node.left, new_node)

        _add_helper(self.root, new_node)

    
    def Contains(self,value):
        """
        Checks if the binary search tree contains a node with the given value.

        Args:
            value: The value to search for.

        Returns:
            True if the value is found, False otherwise.
        """
        def _Contains_helper(node,target_value):
            if node is None:
                return False
            if target_value == node.value:
                return True
            if target_value > node.value:
                return _Contains_helper(node.right, target_value)
            else:
                return _Contains_helper(node.left, target_value)

        return _Contains_helper(self.root, value)   
           

                

        

    

        
















if __name__ == "__main__":
    binary_tree=BinarySearchTree()
    binary_tree.root=TreeNode(23)
    binary_tree.root.left=TreeNode(8)
    binary_tree.root.right=TreeNode(42)
    binary_tree.root.left.left=TreeNode(4)
    binary_tree.root.left.right=TreeNode(16)
    binary_tree.root.right.left=TreeNode(27)
    print(binary_tree.pre_order())
    print(binary_tree.in_order())
    print(binary_tree.post_order())
    binary_tree.add(30)
    print(binary_tree.in_order())
    print(binary_tree.Contains(30))
    print(binary_tree.Contains(97))
