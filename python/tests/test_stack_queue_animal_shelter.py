from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import Dog, Cat, Monkey, AnimalError, AnimalShelter
from stacks_and_queue.error import EmptyError
import pytest

# test animal shelter instance 
def test_shelter():
    shelter = AnimalShelter
    assert shelter
    
# test animals
def test_dog():
    marco = Dog
    assert marco

def test_cat():
    felix = Cat
    assert felix

def test_monkey():
    diddy = Monkey
    assert diddy

# test wrong animal    
def test_input_cat_or_dog():
    shelter = AnimalShelter()
    diddy = Monkey
    with pytest.raises(AnimalError):
        shelter.enqueue(diddy)
        
# test enqueue dog
def test_dog_enq():
    shelter = AnimalShelter()
    milo = Dog('Milo')
    shelter.enqueue(milo)
    actual = shelter.in_stack.peek().name
    expected = 'Milo'
    assert actual == expected
    
# test enqueue cat
def test_cat_enq():
    shelter = AnimalShelter()
    felix = Cat('Felix')
    shelter.enqueue(felix)
    actual = shelter.in_stack.peek().name
    expected = 'Felix'
    assert actual == expected
    
# test empty shelter
def test_empty_shelter():
    shelter = AnimalShelter()
    with pytest.raises(EmptyError):
        shelter.dequeue()
