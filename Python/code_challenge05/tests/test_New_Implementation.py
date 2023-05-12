import pytest
from New_Implementation.New_Implementation import Node ,LinkedList

def test_Empty_Linked_List():
    node1=LinkedList()
    assert node1.head==None

def test_Insert():
    node2=LinkedList("node2")
    node2.insert("node3")
    assert node2.head.value=="node3"

def test_Head_linked_List():
    node1=LinkedList("node1")
    node2=LinkedList()
    node2.insert("node2")
    node2.head.next=node1
    assert node2.head.value=="node2"

def test_Multi_Node():
    Linked_List=LinkedList()
    Linked_List.insert("node1")
    Linked_List.insert("node2")
    Linked_List.insert("node3")
    assert Linked_List.head.value=="node3"

def test_Finding_A_Value_True():
    Linked_List=LinkedList()
    Linked_List.insert("node1")
    Linked_List.insert("node2")
    Linked_List.insert("node3")
    act=Linked_List.includes("node1")
    expect=True
    assert act==expect

def test_Finding_A_Value_False():
    Linked_List=LinkedList()
    Linked_List.insert("node1")
    Linked_List.insert("node2")
    Linked_List.insert("node3")
    act=Linked_List.includes("node5")
    expect=False
    assert act==expect

def test_All_The_Values():
    Linked_List=LinkedList()
    Linked_List.insert("c")
    Linked_List.insert("b")
    Linked_List.insert("a")
    act=Linked_List.ToString()
    expect= "a -> b -> c -> None"
    assert act == expect

