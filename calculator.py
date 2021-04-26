class CalculatorError(Exception):
    """Basic exception for Calculator class"""

class Calculator():
    """Basic calculator"""

    def add(self, a, b):
        try:
            return a + b
        except TypeError:
            raise(CalculatorError)
    
    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b