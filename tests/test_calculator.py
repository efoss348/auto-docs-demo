import pytest
from src.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    """Test addition functionality."""
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3)

def test_multiply(calculator):
    """Test multiplication functionality."""
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(0.1, 0.2) == pytest.approx(0.02)

def test_power(calculator):
    """Test power function."""
    assert calculator.power(2, 3) == 8.0
    assert calculator.power(3, 0.5) == pytest.approx(1.7320508075688772)
    assert calculator.power(2, 0) == 1.0
    assert calculator.power(1000, -1) == 0.001

def test_average(calculator):
    """Test average calculation."""
    assert calculator.average([1, 2, 3, 4, 5]) == 3.0
    assert calculator.average([0, 0, 0]) == 0.0
    assert calculator.average([1.5, 2.5]) == 2.0

def test_standard_deviation(calculator):
    """Test standard deviation calculation."""
    assert calculator.standard_deviation([2, 4, 4, 4, 5, 5, 7, 9]) == pytest.approx(2.0)
    assert calculator.standard_deviation([1, 1, 1, 1]) == 0.0
    assert calculator.standard_deviation([1, 2]) == pytest.approx(0.5)

def test_history(calculator):
    """Test operation history tracking."""
    calculator.add(1, 2)
    calculator.multiply(3, 4)
    history = calculator.get_history()
    assert len(history) == 2
    assert history[0] == "1 + 2 = 3.0"
    assert history[1] == "3 * 4 = 12.0"

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0.1, 0.2, 0.3),
    (1000, 2000, 3000),
])
def test_add_parametrized(calculator, a, b, expected):
    """Parametrized test for addition with various inputs."""
    assert calculator.add(a, b) == pytest.approx(expected)