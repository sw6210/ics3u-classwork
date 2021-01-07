# main
------

def sum_double(a: int, b: int) -> int:
    """Determines the sum of 2 integers.

    Args:
        a: An integer.
        b: Another integer.

    Returns:
        The sum of a and b if they are different values. Double the sum if a and b are the same.
    """

    if a == b:
        return (a + b) * 2
    else:
        return a + b


def diff21(n: int) -> int:
    """Determines absolute difference between n and 21.

    Args:
        n: An integer.

    Returns:
        Difference between n and 21. Doubles the difference if n is larger than 21.
    """

    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2


def parrot_trouble(talking: bool, hour: int) -> bool:
    """Determines whether or not we are in trouble. 

    Args:
        talking: True if parrot is talking
        hour: An integer from 1 to 24

    Returns:
        True if parrot is talking and hour is before 7 or after 20. False otherwise.
    """

    if talking == True and (hour < 7 or hour > 20):
        return True
    else:
        return False


def makes10(a: int, b: int) -> bool:
    """Determines if one of the integers or the sum is equal to 10.

    Args:
        a: An integer.
        b: Another integer.

    Returns:
        True if a or b is 10 or if the sum of a and b is 10. False otherwise.
    """

    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False


def near_hundred(n: int) -> bool:
    """Determines if an integer is within 10 of 100 or 200.

    Args:
        n: An integer.

    Returns:
        True if n is within 10 of 100 or 200. False otherwise.
    """
    
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        return True
    else:
        return False
        

# test
------

from main import sum_double
from main import diff21
from main import parrot_trouble
from main import makes10
from main import near_hundred

def test_sum_double():
    assert sum_double(1, 2) == 3	
    assert sum_double(3, 2) == 5
    assert sum_double(2, 2) == 8	
    assert sum_double(-1, 0) == -1
    assert sum_double(3, 3) == 12


def test_diff21():
    assert diff21(19) == 2	
    assert diff21(10) == 11	
    assert diff21(21) == 0
    assert diff21(22) == 2	
    assert diff21(25) == 8


def test_parrot_trouble():
    assert parrot_trouble(True, 6) == True	
    assert parrot_trouble(True, 7) == False	
    assert parrot_trouble(False, 6) == False
    assert parrot_trouble(True, 21) == True	
    assert parrot_trouble(False, 21) == False


def test_makes10():
    assert makes10(9, 10) == True	
    assert makes10(9, 9) == False	
    assert makes10(1, 9) == True	
    assert makes10(10, 1) == True	
    assert makes10(10, 10) == True


def test_near_hundred():
    assert near_hundred(93) == True
    assert near_hundred(90) == True
    assert near_hundred(89) == False
    assert near_hundred(110) == True
    assert near_hundred(111) == False
