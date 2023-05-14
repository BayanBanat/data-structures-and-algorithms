import pytest
from New_Implementation.New_Implementation import LinkedList,Node

# @pytest.mark.skip()
def test_Empty_Linked_List(linked_list):
    assert linked_list.head == None

# @pytest.mark.skip()
def test_Insert(linked_list):
    linked_list.insert("node2")
    linked_list.insert("node3")
    assert linked_list.head.value == "node3"

# @pytest.mark.skip()
def test_Head_linked_List(linked_list):
    node1=Node("node1")
    linked_list.insert("node2")
    linked_list.head.next=node1
    assert linked_list.head.value=="node2"


# @pytest.mark.skip()
def test_Multi_Node(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    assert linked_list.head.value == "node3"

# @pytest.mark.skip()
def test_Finding_A_Value_True(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    act = linked_list.includes("node1")
    expect = True
    assert act == expect

# @pytest.mark.skip()
def test_Finding_A_Value_False(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    act = linked_list.includes("node5")
    expect = False
    assert act == expect

# @pytest.mark.skip()
def test_All_The_Values(linked_list):
    linked_list.insert("c")
    linked_list.insert("b")
    linked_list.insert("a")
    act = linked_list.ToString()
    expect = "a -> b -> c -> None"
    assert act == expect


@pytest.fixture
def linked_list():
    return LinkedList()