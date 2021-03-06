from code_challenges.hashmap_left_join.hashmap_left_join import left_join
import pytest 

@pytest.mark.skip("pending")
def test_left_join():
    assert left_join

@pytest.mark.skip("pending")    
def test_simple():
    hash_left = {'one': 'car'}
    hash_right = {'one': 'bike'} 
    actual = left_join(hash_left, hash_right)
    expected = {'one': ['car', 'bike']}
    assert actual == expected
 
@pytest.mark.skip("pending")    
def test_no_right():
    hash_left = {'one': 'car'}
    hash_right = {}
    
    actual = left_join(hash_left, hash_right)
    expected = {'one': ['car']}
    assert actual == expected
    
@pytest.mark.skip("pending")    
def test_none():
    hash_left = {'one': 'car', 'two': 'house'}
    hash_right = {'one': 'bike'}
    
    actual = left_join(hash_left, hash_right)
    expected = {'one': ['car', 'bike'], 'two': ['house', None]}
    assert actual == expected
    