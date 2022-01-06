from code_challenges.insertion_sort.insertion_sort import insertion_sort

def test_import():
    assert insertion_sort
    
def test_trace():
    list = [8, 4, 23, 42, 16, 15]
    actual = insertion_sort(list)
    assert actual == [4, 8, 15, 16, 23, 42]
    
def test_simple():
    list = [5, 3, 1]
    actual = insertion_sort(list)
    assert actual == [1, 3, 5]
    
def test_duplicate():
    list = [1, 5, 1, 8]
    actual = insertion_sort(list)
    assert actual == [1, 1, 5, 8]