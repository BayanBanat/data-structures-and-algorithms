from insertion import insert, insertion_sort

def test_insertion_sort():
    input_array = [8, 4, 23, 42, 16, 15]
    sorted_array = insertion_sort(input_array)
    assert sorted_array == [4, 8, 15, 16, 23, 42]



