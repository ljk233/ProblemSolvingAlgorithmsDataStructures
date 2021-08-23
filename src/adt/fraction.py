
"""
"""


from __future__ import annotations
from typing import Tuple


def gcd(m: int, n: int) -> int:
    """
    Implementation of the Euclid’s Algorithm

    return
    ======
    int, the gcd of m and n
    """

    old_m: int = 0
    old_n: int = 0

    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n

    return n


class Fraction:
    """
    A class to model a fraction.

    The operations for the Fraction type will allow a Fraction data
    object to behave like any other numeric value. We need to be able
    to add, subtract, multiply, and divide fractions.
    We also want to be able to show fractions using the standard
    “slash” form, for example "3/5".

    In addition, all fraction methods should return results in their
    lowest terms so that no matter what computation is performed,
    we always end up with the most common form.
    """

    def __init__(self, top: int, bottom: int) -> None:
        """
        Initialises an object of type Fraction. Fraction is stored in
        its lowest terms.

        params
        ======
        top, int
            fraction numerator
        bottom, int
            faction denomenator
        """
        common: int = gcd(top, bottom)
        self.num: int = top // common
        self.den: int = bottom // common

    def __str__(self) -> str:
        """
        return
        ======
        str, the fraction represented by the object in its classic
        "slash form, e.g., "3/5"
        """
        return f"{self.num}/{self.den}"

    # arithmetic operators

    def __add__(self, other_fraction: Fraction) -> Fraction:
        """
        return
        ======
        Fraction, the sum of the receiver and other_fraction
        """
        new_num: int = (
            (self.num * other_fraction.den) + (self.den * other_fraction.num))
        new_den: int = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __sub__(self, other_fraction: Fraction) -> Fraction:
        """
        return
        ======
        Fraction, the difference between the receiver and other_fraction
        """
        new_num: int = (
            (self.num * other_fraction.den) - (self.den * other_fraction.num))
        new_den: int = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __mul__(self, other_fraction: Fraction) -> Fraction:
        """
        return
        ======
        Fraction, the sum of the receiver and other_fraction
        """
        new_num: int = self.num * other_fraction.num
        new_den: int = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction: Fraction) -> Fraction:
        """
        return
        ======
        Fraction, the sum of the receiver and other_fraction
        """
        new_num: int = self.num * other_fraction.den
        new_den: int = self.den * other_fraction.num
        return Fraction(new_num, new_den)

    def __eq__(self, other_fraction: Fraction) -> bool:
        """
        return
        ======
        bool, true if the two objects represent the same fraction,
        otherwise false
        """

        first_num: int = self.num * other_fraction.den
        second_num: int = other_fraction.num * self.den
        return first_num == second_num

    # relational operators

    def _cross_multiply(self, other_fraction: Fraction) -> Tuple(int):
        """
        return
        ======
        tuple(int), the two products resulting from cross-multiplaction
        of the two fractions
        """
        return (self.num * other_fraction.den, self.den, other_fraction.num)

    def __le__(self, other_fraction: Fraction) -> bool:
        """
        return
        ======
        bool, true if the receiver is less than or equal to the other fraction,
        otherwise false
        """
        prod: Tuple(int) = self._cross_multiply(other_fraction)
        return prod[0] <= prod[1]

    def __lt__(self, other_fraction: Fraction) -> bool:
        """
        return
        ======
        bool, true if the receiver is less than the other fraction,
        otherwise false
        """
        prod: Tuple(int) = self._cross_multiply(other_fraction)
        return prod[0] < prod[1]

    def __ge__(self, other_fraction: Fraction) -> bool:
        """
        return
        ======
        bool, true the receiver is greater than or equal to the other
        fraction, otherwise false
        """
        prod: Tuple(int) = self._cross_multiply(other_fraction)
        return prod[0] >= prod[1]

    def __gt__(self, other_fraction: Fraction) -> bool:
        """
        return
        ======
        bool, true if the receiver is greater than the other fraction,
        otherwise false
        """
        prod: Tuple(int) = self._cross_multiply(other_fraction)
        return prod[0] > prod[1]
