from math_series import __version__ 
from math_series.series import fibonacci
from math_series.series import lukas
from math_series.series import sum_series
def test_version():
    assert __version__ == "0.1.0"
    # Testing Fibonacci series
def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

      # Testing Lukas series
      # Lukas series is : 2, 1, 3, 4, 7, 11, 18, 29
def test_lukas_zero():
    actual = lukas(0)
    expected = 2
    assert actual == expected

def test_lukas_one():
    actual = lukas(1)
    expected = 1
    assert actual == expected

def test_lukas_two():
    actual = lukas(2)
    expected = 3
    assert actual == expected

def test_lukas_three():
    actual = lukas(3)
    expected = 4
    assert actual == expected

def test_lukas_seven():
    actual = lukas(7)
    expected = 29
    assert actual == expected

# Testing sum_series function
def test_sum_series_seven():
    actual = sum_series(7)
    expected = 13
    assert actual == expected

def test_sum_series_seven():
    actual = sum_series(7,2,1)
    expected = 29
    assert actual == expected
    