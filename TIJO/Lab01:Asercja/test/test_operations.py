
from src.operations import max, add, perfect

def test_add():

    #arrange
    first = 1
    second = 3
    expected = 4

    #act
    result = add(first, second)

    #assert
    assert result == expected, f"expected {expected}, got {result}"

def test_max():
    #arrange
    digits = [3,7,2,1,33,4,3]
    expected = 33

    #act
    result = max(digits)

    #assert
    assert result == expected, "success"

def test_max_single():
    #arrange
    digits = [2]
    expected=2

    #act
    result =max(digits)

    #assert
    assert result == expected, 'success'

def test_max_none():
    #arrange
    digits = None
    expected = None

    #act
    result = max(digits)

    #assert
    assert result == expected, 'success'

def test_max_empty():
    #arrange
    digits=[]
    expected = None

    #act
    result = max(digits)

    #assert
    assert result == expected, 'success'

def test_no_perfect():
    #arrange
    digit = 7
    expected = False

    #act
    result = perfect(digit)

    assert result == expected, 'success'

def test_perfect():
    #arrange
    digit = 6
    expected = True

    #act
    result = perfect(digit)

    #assert
    assert result == expected, 'success'


if __name__ == "__main__":
    test_add()
    test_max()
    test_max_none()
    test_max_single()
    test_max_empty()
    test_perfect()
    test_no_perfect()