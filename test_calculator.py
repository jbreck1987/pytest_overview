#Pytest works based off of creating functions that test OTHER functions in your code
#NOTE: Functions AND test files must start with 'test'

import pytest
from calculator import Calculator, CalculatorError
def test_add():
    #Break test functions into sections
    #Arrange(I.E. create objects, etc.)
    calc = Calculator()
    
    #Do the action that you want to test(E.g. add numbers) where
    #the result is KNOWN
    result = calc.add(1, 1)

    #Test your assertion about what the value should be
    assert result == 2

def test_subtract():
    #Break test functions into sections
    #Arrange(I.E. create objects, etc.)
    calc = Calculator()
    
    #Do the action that you want to test(E.g. add numbers) where
    #the result is KNOWN
    result = calc.sub(1, 1)

    #Test your assertion about what the value should be
    assert result == 0

def test_multiply():
    #Break test functions into sections
    #Arrange(I.E. create objects, etc.)
    calc = Calculator()
    
    #Do the action that you want to test(E.g. add numbers) where
    #the result is KNOWN
    result = calc.multiply(1, 1)

    #Test your assertion about what the value should be
    assert result == 1

def test_add_type_error():
    #Sometimes useful to test whether your code throws the correct exception
    # (or even catches them) in weird cases
    calc = Calculator()
    
    # Can catch exceptions in pytest context manager
    with pytest.raises(CalculatorError):
        calc.add('1', 1) 
