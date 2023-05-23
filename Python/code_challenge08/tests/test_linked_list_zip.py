
import pytest
# from Python.code_challenge05.New_Implementation.New_Implementation import LinkedList
# from Python.code_challenge08.linked_list_zip.linked_list_zip import linked_list_zip
from linked_list_zip.linked_list_zip import LinkedList,linked_list_zip


@pytest.fixture
def linked_list():
    return LinkedList()

@pytest.fixture
def linked_list2():
    return LinkedList()


def test_linked_list_zip(linked_list, linked_list2):
    linked_list.append("2")
    linked_list.append("3")
    linked_list.append("1")
    linked_list2.append("4")
    linked_list2.append("9")
    linked_list2.append("5")

    expected_result = "2 -> 4 -> 3 -> 9 -> 1 -> 5 -> None"
    assert linked_list_zip(linked_list, linked_list2).ToString() == expected_result

# @pytest.mark.skip()
def test_linked_list_zip_different_length1(linked_list, linked_list2):
    linked_list.append("3")
    linked_list.append("1")
    linked_list2.append("4")
    linked_list2.append("9")
    linked_list2.append("5")

    expected_result = "3 -> 4 -> 1 -> 9 -> 5 -> None"
    assert linked_list_zip(linked_list, linked_list2).ToString() == expected_result

# @pytest.mark.skip()
def test_linked_list_zip_different_length2(linked_list, linked_list2):
    linked_list.append("2")
    linked_list.append("3")
    linked_list.append("1")
    linked_list2.append("9")
    linked_list2.append("5")

    expected_result = "2 -> 9 -> 3 -> 5 -> 1 -> None"
    assert linked_list_zip(linked_list, linked_list2).ToString() == expected_result

# @pytest.mark.skip()
def test_linked_list_zip_one_empty1(linked_list, linked_list2):
    linked_list.append("2")
    linked_list.append("3")
    linked_list.append("1")

    expected_result = "2 -> 3 -> 1 -> None"
    assert linked_list_zip(linked_list, linked_list2).ToString() == expected_result

# @pytest.mark.skip()
def test_linked_list_zip_one_empty2(linked_list, linked_list2):
    linked_list2.append("4")
    linked_list2.append("5")
    linked_list2.append("6")

    expected_result = "4 -> 5 -> 6 -> None"
    assert linked_list_zip(linked_list, linked_list2).ToString() == expected_result



