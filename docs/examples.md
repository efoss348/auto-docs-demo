# Usage Examples

## Basic Operations

```python
from calculator import Calculator

# Create a calculator instance
calc = Calculator()

# Basic arithmetic
print(calc.add(5, 3))       # Output: 8.0
print(calc.multiply(4, 6))  # Output: 24.0

# Power operations
print(calc.power(2, 3))     # Output: 8.0 (2 cubed)
print(calc.power(16, 0.5))  # Output: 4.0 (square root of 16)
```

## Statistical Operations

```python
from calculator import Calculator

calc = Calculator()

# Sample dataset: daily temperatures
temperatures = [20.5, 21.0, 23.5, 22.0, 19.5, 20.0, 21.5]

# Calculate average temperature
avg_temp = calc.average(temperatures)
print(f"Average temperature: {avg_temp:.1f}°C")  # Output: 21.1°C

# Calculate temperature variation (standard deviation)
temp_variation = calc.standard_deviation(temperatures)
print(f"Temperature variation: {temp_variation:.1f}°C")  # Output: 1.3°C
```

## Operation History

```python
from calculator import Calculator

calc = Calculator()

# Perform some calculations
calc.add(10, 5)
calc.power(2, 8)
calc.average([1, 2, 3, 4, 5])

# Print operation history
print("Calculation History:")
for operation in calc.get_history():
    print(f"  {operation}")

# Output:
# Calculation History:
#   10 + 5 = 15.0
#   2 ^ 8 = 256.0
#   avg([1, 2, 3, 4, 5]) = 3.0
```

## Real-World Example: Data Analysis

```python
from calculator import Calculator

def analyze_student_scores(scores):
    """Analyze a set of student test scores."""
    calc = Calculator()
    
    # Calculate statistics
    avg_score = calc.average(scores)
    score_spread = calc.standard_deviation(scores)
    highest_possible = calc.power(10, 2)  # Test scored out of 100
    
    # Print analysis
    print(f"Class Analysis:")
    print(f"Average Score: {avg_score:.1f}")
    print(f"Score Variation: ±{score_spread:.1f}")
    print(f"Percentage of Maximum: {(avg_score/highest_possible)*100:.1f}%")

# Example usage
student_scores = [85, 92, 78, 95, 89, 88, 91, 76, 88, 82]
analyze_student_scores(student_scores)
```