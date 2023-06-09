# Code Challenge: Class 15
# Trees


## Approach & Efficiency

**pre_order():**Time Complexity: O(n), where n is the number of nodes in the binary tree. The function visits each node exactly once during the pre-order traversal.
Space Complexity: O(h), where h is the height of the binary tree. The space is used for the recursive call stack.

**in_order():**Time Complexity: O(n), where n is the number of nodes in the binary tree. The function visits each node exactly once during the in-order traversal.
Space Complexity: O(h), where h is the height of the binary tree. The space is used for the recursive call stack.

**post_order():**Time Complexity: O(n), where n is the number of nodes in the binary tree. The function visits each node exactly once during the post-order traversal.
Space Complexity: O(h), where h is the height of the binary tree. The space is used for the recursive call stack.

**add():** Time complexity: O(log n), where n is the number of nodes in the tree. This is because with each comparison, the search space is effectively halved as we traverse down the tree to find the appropriate position to add the new node.
Space Complexity: O(1). The function uses a constant amount of space for creating the new node and variables.

**Contains():** Time complexity: O(log n), where n is the number of nodes in the tree. This is because with each comparison, the search space is effectively halved as we traverse down the tree to find the appropriate position to add the new node.
Space Complexity: O(1). The function uses a constant amount of space for variables and does not use additional space proportional to the input size.

## Solution
python Python/code_challenge15/trees/trees.py     

```python
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
```