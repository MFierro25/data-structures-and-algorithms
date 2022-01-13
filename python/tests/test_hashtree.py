import pytest
from hashtable.hashtable import Hashtable
from hashtable.error import EmptyError

def test_table():
    assert Hashtable
    
# Adding a key/value to your hashtable results in the value being in the data structure
def test_hash_add():
    ht = Hashtable()
    ht.add('car', 'toyota')
    assert ht.contains('car') == True
    
# Retrieving based on a key returns the value stored
def test_hash_get():
    ht = Hashtable()
    ht.add('car', 'toyota')
    assert ht.get('car') == 'toyota'
    
# Successfully returns null for a key that does not exist in the hashtable
def test_no_key():
    ht = Hashtable()
    with pytest.raises(EmptyError):
        ht.get('car')
    
# Successfully handle a collision within the hashtable
def test_collision():
    ht = Hashtable()
    ht.add('car', 'honda')
    ht.add('rac', 'toyota')
    assert ht.contains('car') == True
    assert ht.contains('rac') == True
    assert ht.hash('car') == ht.hash('rac')
    
    
# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_collision_value():
    ht = Hashtable()
    ht.add('car', 'honda')
    ht.add('rac', 'toyota')
    assert ht.get('car') == 'honda'
    assert ht.hash('car') == ht.hash('rac')