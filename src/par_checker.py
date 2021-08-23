
# %%
from __future__ import annotations
from .adt.pyliststack import Stack


# %%
def par_checker(expression: str) -> bool:
    """
    Check if a series of parentheses are balanced.

    Will not supply correct answer if expression contains mixed bracket
    types.

    Args:
        symbol_str (`str`): collection of nested parentheses that is to
        be checked.
        Example "(()())()(())"

    Returns:
        `bool`: True if the expression has balanced parentheses,
        otherwise False
    """
    symbol_stack: Stack = Stack()
    is_balanced: bool = True
    ndx: int = 0

    while is_balanced and ndx < len(expression):
        paren: str = expression[ndx]
        if paren == "(":
            symbol_stack.push(paren)
        elif not symbol_stack.is_empty():
            symbol_stack.pop()
        else:
            is_balanced = False
        ndx += 1

    return symbol_stack.is_empty() and is_balanced
