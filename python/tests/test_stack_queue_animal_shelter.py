from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import Dog, Cat, Monkey, AnimalError, AnimalShelter
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
    shelter = AnimalShelter
    diddy = Monkey
    with pytest.raises(AnimalError):
        shelter.enqueue(diddy, Monkey)