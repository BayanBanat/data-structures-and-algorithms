from tree_max.tree_max import BStTree, TNode

def test_tree_max():
    binary_tree=BStTree()
    binary_tree.root=TNode(2)
    binary_tree.root.left=TNode(7)
    binary_tree.root.right=TNode(5)
    binary_tree.root.left.left=TNode(2)
    binary_tree.root.left.right=TNode(6)
    binary_tree.root.left.right.right=TNode(11)
    binary_tree.root.right.right=TNode(9)
    binary_tree.root.right.right.left=TNode(4)
    assert binary_tree.tree_max() == 11