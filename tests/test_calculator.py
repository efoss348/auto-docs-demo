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

def test_history(calculator):
    """Test operation history tracking."""
    calculator.add(1, 2)
    calculator.multiply(3, 4)
    history = calculator.get_history()
    assert len(history) == 2
    assert history[0] == "1 + 2 = 3"
    assert history[1] == "3 * 4 = 12"

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0.1, 0.2, 0.3),
    (1000, 2000, 3000),
])
def test_add_parametrized(calculator, a, b, expected):
    """Parametrized test for addition with various inputs."""
    assert calculator.add(a, b) == pytest.approx(expected)