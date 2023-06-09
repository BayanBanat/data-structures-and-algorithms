import pytest
from trees.trees import BinarySearchTree, TreeNode

def test_empty_tree(new_tree):
    assert new_tree.root is None

def test_single_root_node(new_tree):
    new_tree.root = TreeNode(10)
    assert new_tree.root.value == 10

def test_add_a_left_child(new_tree):
    new_tree.root = TreeNode(23)
    new_tree.root.left=TreeNode(8)
    new_tree.root.right=TreeNode(42)
    new_tree.root.left.left=TreeNode(4)
    new_tree.root.left.right=TreeNode(16)
    new_tree.root.right.left=TreeNode(27)
    new_tree.add(2)
    assert new_tree.in_order() == [2,4, 8, 16, 23, 27, 42]

def test_add_a_right_child(new_tree):
    new_tree.root = TreeNode(23)
    new_tree.root.left=TreeNode(8)
    new_tree.root.right=TreeNode(42)
    new_tree.root.left.left=TreeNode(4)
    new_tree.root.left.right=TreeNode(16)
    new_tree.root.right.left=TreeNode(27)
    new_tree.add(30)
    assert new_tree.in_order() == [4, 8, 16, 23, 27,30, 42]


def test_pre_order_traversal(new_tree):
    new_tree.root = TreeNode(23)
    new_tree.root.left=TreeNode(8)
    new_tree.root.right=TreeNode(42)
    new_tree.root.left.left=TreeNode(4)
    new_tree.root.left.right=TreeNode(16)
    new_tree.root.right.left=TreeNode(27)
    assert new_tree.pre_order() == [23, 8, 4, 16, 42, 27]


def test_in_order_traversal(new_tree):
    new_tree.root = TreeNode(23)
    new_tree.root.left=TreeNode(8)
    new_tree.root.right=TreeNode(42)
    new_tree.root.left.left=TreeNode(4)
    new_tree.root.left.right=TreeNode(16)
    new_tree.root.right.left=TreeNode(27)
    assert new_tree.in_order() == [4, 8, 16, 23, 27, 42]



def test_post_order_traversal(new_tree):
    new_tree.root = TreeNode(23)
    new_tree.root.left=TreeNode(8)
    new_tree.root.right=TreeNode(42)
    new_tree.root.left.left=TreeNode(4)
    new_tree.root.left.right=TreeNode(16)
    new_tree.root.right.left=TreeNode(27)
    assert new_tree.post_order() == [4, 16, 8, 27, 42, 23]



def test_contains_exist(new_tree):
    new_tree.root = TreeNode(23)
    new_tree.root.left=TreeNode(8)
    new_tree.root.right=TreeNode(42)
    new_tree.root.left.left=TreeNode(4)
    new_tree.root.left.right=TreeNode(16)
    new_tree.root.right.left=TreeNode(27)
    assert new_tree.Contains(42)

def test_contains_not_exist(new_tree):
    new_tree.root = TreeNode(23)
    new_tree.root.left=TreeNode(8)
    new_tree.root.right=TreeNode(42)
    new_tree.root.left.left=TreeNode(4)
    new_tree.root.left.right=TreeNode(16)
    new_tree.root.right.left=TreeNode(27)
    assert not new_tree.Contains(55) 

@pytest.fixture
def new_tree():
    return BinarySearchTree()