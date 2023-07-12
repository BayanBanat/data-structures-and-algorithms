
from merge import  merge_sort

def test_merge_sort():
    input_array = [8, 4, 23, 42, 16, 15]
    merge_sort(input_array)
    assert input_array == [4, 8, 15, 16, 23, 42]


def test_Reverse_sorted():
    input_array = [20, 18, 12, 8, 5, -2]
    merge_sort(input_array)
    assert input_array == [-2, 5, 8, 12, 18, 20]

def test_Few_uniques():
    input_array = [5, 12, 7, 5, 5, 7]
    merge_sort(input_array)
    assert input_array == [5, 5, 5, 7, 7, 12]


def test_Nearly_sorted():
    input_array = [2, 3, 5, 7, 13, 11]
    merge_sort(input_array)
    assert input_array == [2, 3, 5, 7, 11, 13]