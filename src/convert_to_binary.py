
# %%
from __future__ import annotations
from .adt.pyliststack import Stack


# %%
def convert_to_binary(decimal: int) -> str:
    """
    Converts a decimal integer into its binary form, using the divide
    by 2 algorithm

    Args:
        decimal (int): decimal integer to be converted.

    Returns:
        str: binary representation of the decimal number.
    """
    binary_string: str = str()
    remainders: Stack = Stack()
    while decimal > 0:
        remainders.push(decimal % 2)
        decimal = decimal // 2

    while not remainders.is_empty():
        remainder: int = remainders.pop()
        binary_string = binary_string + str(remainder)

    return binary_string
