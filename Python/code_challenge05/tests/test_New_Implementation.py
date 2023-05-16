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

def test_Add_Node_At_End(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    linked_list.append("node4")
    new_string="node3 -> node2 -> node1 -> node4 -> None"
    assert linked_list.ToString()==new_string

def test_Add_Multi_Node_At_End(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    linked_list.append("node4")
    linked_list.append("node5")
    new_string="node3 -> node2 -> node1 -> node4 -> node5 -> None"
    assert linked_list.ToString()==new_string

def test_Insert_Before(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    linked_list.insert_before("node2","node4")
    new_string="node3 -> node4 -> node2 -> node1 -> None"
    assert linked_list.ToString()==new_string

def test_Insert_Before_First_Node(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    linked_list.insert_before("node3","node4")
    new_string="node4 -> node3 -> node2 -> node1 -> None"
    assert linked_list.ToString()==new_string
 
def test_Insert_Before_Value_If_Does_Not_Exist(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    linked_list.insert_before("node6","node4")
    new_string="node3 -> node2 -> node1 -> None"
    assert linked_list.ToString()==new_string


def test_Insert_After_Value(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    linked_list.Insert_After("node2","node4")
    new_string="node3 -> node2 -> node4 -> node1 -> None"
    assert linked_list.ToString()==new_string

def test_Insert_After_The_End_Value(linked_list):
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.Insert_After(1,4)
    new_string="3 -> 2 -> 1 -> 4 -> None"
    assert linked_list.ToString()==new_string

def test_Insert_After_Value_If_Does_Not_Exist(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    linked_list.Insert_After("node6","node4")
    new_string="node3 -> node2 -> node1 -> None"
    assert linked_list.ToString()==new_string

def test_linked_list_kth_Exciption_and_sameLength(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    try:
        linked_list.linked_list_kth(6)
    except ValueError as err:
        assert str(err)=="Invalid value of k"
    

# def test_linked_list_kth_sameLength(linked_list):
#     linked_list.insert("node1")
#     linked_list.insert("node2")
#     linked_list.insert("node3")
#     assert linked_list.linked_list_kth(3) == "node3"    

def test_linked_list_kth_last_index(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    assert linked_list.linked_list_kth(-1) == "node3"

def test_linked_list_kth_one_size(linked_list):
    linked_list.insert("node1")
    assert linked_list.linked_list_kth(0) == "node1"

def test_linked_list_kth_Middle(linked_list):
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    assert linked_list.linked_list_kth(1) == "node2"


@pytest.fixture
def linked_list():
    return LinkedList()