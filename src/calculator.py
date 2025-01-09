"""A simple calculator module to demonstrate documentation."""

class Calculator:
    """A basic calculator class with arithmetic operations.
    
    This class provides basic arithmetic operations and serves as an example
    for documentation generation.
    
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
        result = a + b
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
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def get_history(self) -> list:
        """Get the history of operations.
        
        Returns:
            list: A list of strings representing the history of operations
        """
        return self.history