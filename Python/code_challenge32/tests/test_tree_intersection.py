import pytest

from tree_intersection.tree_intersection import tree_intersection,BinaryTree,TreeNode

def test_tree_intersection1():
    BT1 = BinaryTree()
    BT1.root = TreeNode(5)
    BT1.root.left = TreeNode(3)
    BT1.root.right = TreeNode(8)
    BT2 = BinaryTree()
    BT2.root = TreeNode(8)
    BT2.root.left = TreeNode(3)
    BT2.root.right = TreeNode(12)
    intersection_set = tree_intersection(BT1, BT2)
    assert intersection_set==[3,8]
    
def test_tree_intersection2():
    BT1 = BinaryTree()
    BT1.root = TreeNode(5)
    BT1.root.left = TreeNode(31)
    BT1.root.right = TreeNode(8)
    BT2 = BinaryTree()
    BT2.root = TreeNode(81)
    BT2.root.left = TreeNode(3)
    BT2.root.right = TreeNode(12)
    intersection_set = tree_intersection(BT1, BT2)
    assert intersection_set==[]

def test_tree_intersection3():
    BT1 = BinaryTree()
    BT1.root = TreeNode(5)
    BT1.root.left = TreeNode(6)
    BT1.root.right = TreeNode(7)
    BT2 = BinaryTree()
    BT2.root = TreeNode(5)
    BT2.root.left = TreeNode(6)
    BT2.root.right = TreeNode(7)
    intersection_set = tree_intersection(BT1, BT2)
    assert intersection_set==[6, 5, 7]
    

def test_tree_intersection4():
    BT1 = BinaryTree()
    BT1.root = TreeNode(150)
    BT1.root.left = TreeNode(100)
    BT1.root.right = TreeNode(250)
    BT1.root.left.left = TreeNode(75)
    BT1.root.left.right = TreeNode(160)
    BT1.root.left.right.left = TreeNode(125)
    BT1.root.left.right.right = TreeNode(175)
    BT1.root.right.left = TreeNode(200)
    BT1.root.right.right = TreeNode(350)
    BT1.root.right.right.left = TreeNode(300)
    BT1.root.right.right.right = TreeNode(500)

    BT2 = BinaryTree()
    BT2.root = TreeNode(42)
    BT2.root.left = TreeNode(100)
    BT2.root.right = TreeNode(600)
    BT2.root.left.left = TreeNode(15)
    BT2.root.left.right = TreeNode(160)
    BT2.root.left.right.left = TreeNode(125)
    BT2.root.left.right.right = TreeNode(175)
    BT2.root.right.left = TreeNode(200)
    BT2.root.right.right = TreeNode(350)
    BT2.root.right.right.left = TreeNode(4)
    BT2.root.right.right.right = TreeNode(500)

    intersection_set = tree_intersection(BT1, BT2)
    assert intersection_set==[100, 125, 160, 175, 200, 350, 500]


