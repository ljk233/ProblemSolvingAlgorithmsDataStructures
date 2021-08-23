
# %%
from __future__ import annotations
from .adt.pyliststack import Stack


# %%
def convert_to_base(decimal: int, base: int) -> str:
    """
    Converts a decimal integer into its string representation in
    any base.

    Only imlemented for up to and including base-36.

    Args:
        decimal (`int`): decimal integer number to be converted.
                         base (`int`): base to convert the decimal
                         integer.

    Returns:
        `str`: base representation of the decimal integer.
    """
    remainders: Stack = Stack()
    digits: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret_str: str = str()

    while decimal > 0:
        remainders.push(decimal % base)
        decimal = decimal // base

    while not remainders.is_empty():
        a_remainder: int = remainders.pop()
        a_digit: str = digits[a_remainder]
        ret_str = ret_str + a_digit

    return ret_str
