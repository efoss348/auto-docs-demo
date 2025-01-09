"""A simple calculator module to demonstrate documentation."""
from typing import List

class Calculator:
    """A basic calculator class with arithmetic and statistical operations.
    
    This class provides basic arithmetic operations and statistical calculations.
    All operations are automatically logged in the history.
    
    Attributes:
        history (list): A list of all operations performed
    """
    
    def __init__(self):
        """Initialize a new Calculator instance."""
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
        
        Returns:
            float: The sum of a and b
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
        """
        result = float(a + b)
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
        
        Returns:
            float: The product of a and b
        
        Example:
            >>> calc = Calculator()
            >>> calc.multiply(2, 3)
            6.0
        """
        result = float(a * b)
        self.history.append(f"{a} * {b} = {result}")
        return result

    def power(self, base: float, exponent: float) -> float:
        """Raise a number to a power.
        
        Args:
            base (float): The base number
            exponent (float): The exponent to raise the base to
        
        Returns:
            float: base raised to the power of exponent
        
        Example:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8.0
            >>> calc.power(3, 0.5)  # Square root of 3
            1.7320508075688772
        """
        result = float(base ** exponent)
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result

    def average(self, numbers: List[float]) -> float:
        """Calculate the arithmetic mean of a list of numbers.
        
        Args:
            numbers (List[float]): List of numbers to average
        
        Returns:
            float: The arithmetic mean
        
        Example:
            >>> calc = Calculator()
            >>> calc.average([1, 2, 3, 4, 5])
            3.0
        """
        result = float(sum(numbers)) / len(numbers)
        self.history.append(f"avg({numbers}) = {result}")
        return result

    def standard_deviation(self, numbers: List[float]) -> float:
        """Calculate the population standard deviation of a list of numbers.
        
        Args:
            numbers (List[float]): List of numbers to calculate std dev for
        
        Returns:
            float: The population standard deviation
        
        Example:
            >>> calc = Calculator()
            >>> calc.standard_deviation([2, 4, 4, 4, 5, 5, 7, 9])
            2.0
        """
        mean = self.average(numbers)
        squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
        result = float((squared_diff_sum / len(numbers)) ** 0.5)
        self.history.append(f"std_dev({numbers}) = {result}")
        return result
    
    def get_history(self) -> list:
        """Get the history of operations.
        
        Returns:
            list: A list of strings representing the history of operations
        """
        return self.history