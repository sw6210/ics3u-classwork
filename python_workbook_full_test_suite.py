# main
------

from math import sqrt

# Exercise 81
def hypoteneuse(a: float, b: float) -> float:
    """Determines the hypoteneuse given the two shorter side lengths.

    Args:
        a: A side length.
        b: Another side length.

    Returns:
        The square root of a squared plus b squared.
    """

    return round(sqrt(a*a + b*b), 2)


# Exercise 82
base_fare = 4.00
rate = 0.25

def total_fare(distance: float) -> float:
    """Determines the total fare given distance travelled.

    Args:
        distance: Distance travelled in kilometres.

    Returns:
        Base fare plus rate times distance.
    """

    return round(base_fare + rate * (distance / 0.14), 2)


# Exercise 83
first_item = 10.95
subsequent_item = 2.95

def shipping_charge(items: int) -> float:
    """Determines cost for shipping.

    Args:
        items: Number of items being purchased.

    Returns:
        Shipping cost for first item plus cost for each subsequent item.
    """

    return round(first_item + subsequent_item * (items - 1), 2)


# Exercise 84
def median(a: int, b: int, c: int) -> int:
    """Determines the median given 3 integers.

    Args:
        a: An integer.
        b: Another integer.
        c: Another integer.

    Returns:
        The integer value that lies at the midpoint of the 3 integers.
    """

    return a + b + c - min(a, b, c) - max(a, b, c)


# Exercise 85
def get_ordinal(a: int) -> str:
    """Determines the ordinal name given an integer.

    Args:
        a: An integer from 1 to 12.

    Returns:
        Ordinal name if integer is between 1 and 12. Blank otherwise.
    """

    ordinal_map = [
        "",
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"
    ]
    if a == 0 or a > 12:
        return ""
    return ordinal_map[a]
    

# test
------

from main import hypoteneuse
from main import total_fare
from main import shipping_charge
from main import median
from main import get_ordinal


def test_hypoteneuse():
    assert hypoteneuse(3, 4) == 5
    assert hypoteneuse(5, 12) == 13
    assert hypoteneuse(5.2, 8.9) == 10.31
    assert hypoteneuse(20, 21) == 29 
    assert hypoteneuse(5, 7) == 8.60


def test_total_fare():
    assert total_fare(1) == 5.79
    assert total_fare(2) == 7.57
    assert total_fare(3) == 9.36
    assert total_fare(10) == 21.86
    assert total_fare(15) == 30.79


def test_shipping_charge():
    assert shipping_charge(1) == 10.95
    assert shipping_charge(2) == 13.90
    assert shipping_charge(3) == 16.85
    assert shipping_charge(5) == 22.75
    assert shipping_charge(8) == 31.60


def test_median():
    assert median(1, 2, 3) == 2
    assert median(3, 1, 9) == 3
    assert median(9, 8, 4) == 8
    assert median(21, 57, 42) == 42
    assert median(72, 83, 12) == 72


def test_get_ordinal():
    assert get_ordinal(1) == "first"
    assert get_ordinal(5) == "fifth"
    assert get_ordinal(3) == "third"
    assert get_ordinal(14) == ""
    assert get_ordinal(12) == "twelfth"
