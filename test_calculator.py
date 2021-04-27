#Pytest works based off of creating functions that test OTHER functions in your code
#NOTE: Functions AND test files must start with 'test'

import pytest
from calculator import Calculator, CalculatorError
def test_add():
    #break test functions into sections
    #arrange(i.e. create objects, etc.)
    calc = Calculator()
    
    #do the action that you want to test(e.g. add numbers) where
    #the result is known
    result = calc.add(1, 1)

    #test your assertion about what the value should be
    assert result == 2

# To test multiple input values you can use a built-in pytest decorator called parametrize
# and decorate whatever test you want to send multiple values into.
# NOTE: For loops would seem easier, but the execution breaks out of loops
# after the first FAIL (may not try all cases)
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (0, 0, 0),
        (1, 1, 2),
        (1, -1, 0),
        (-1, -1, -2)
    ]
)
def test_add_multiple(a, b, expected):
    #break test functions into sections
    #arrange(i.e. create objects, etc.)
    calc = Calculator()
    
    #do the action that you want to test(e.g. add numbers) where
    #the result is known
    result = calc.add(a, b)

    #test your assertion about what the value should be
    assert result == expected


def test_add_type_error():
    #Sometimes useful to test whether your code throws the correct exception
    # (or even catches them) in weird cases
    calc = Calculator()
    
    # Can catch exceptions in pytest context manager
    with pytest.raises(CalculatorError):
        calc.add('1', 1) 
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


# Fixtures are used to "setup" an environment so that more complicated functions can be tested
# E.g. Creating numpy arrays of a certain size and type, database creation, etc.
# They are designed to be portable; used for different tests. Fixures are actually defined in
# another file called conftest.py and then called here.
def test_fixture_42(my_fixture):
    assert my_fixture == 42
