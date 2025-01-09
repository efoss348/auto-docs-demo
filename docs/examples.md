# Usage Examples

## Basic Calculator Operations

```python
from calculator import Calculator

# Create a calculator instance
calc = Calculator()

# Addition
result = calc.add(5, 3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8

# Multiplication
result = calc.multiply(4, 6)
print(f"4 * 6 = {result}")  # Output: 4 * 6 = 24

# Check operation history
print("Operation History:")
for operation in calc.get_history():
    print(operation)
```

## Using in Your Project

```python
from calculator import Calculator

def process_calculations(numbers: list[float]) -> list[float]:
    calc = Calculator()
    results = []
    
    for i in range(len(numbers) - 1):
        sum_result = calc.add(numbers[i], numbers[i + 1])
        results.append(sum_result)
    
    return results

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
results = process_calculations(numbers)
print(f"Processed results: {results}")
```