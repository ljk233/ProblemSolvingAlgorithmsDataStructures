
# %%
from __future__ import annotations
from .adt.pyliststack import Stack


# %%
def bracket_checker(expression: str) -> bool:
    """
    Check if a series of brackets are balanced, that is each opening
    symbol has a corresponding closing symbol and the pairs of
    parentheses are properly nested.

    Args:
        expression (`str`): expression that is to be checked for balanced
        brackets.

    Returns:
        `bool`: true if the exressin has balanced brackets, otherwise
        false.
    """
    open_brackets: str = "([{"
    close_brackets: str = ")]}"
    symbol_stack: Stack = Stack()

    is_balanced: bool = True
    ndx: int = 0
    while is_balanced and ndx < len(expression):
        bracket: str = expression[ndx]
        if bracket in open_brackets:
            symbol_stack.push(bracket)
        elif not symbol_stack.is_empty():
            open: str = open_brackets.index(symbol_stack.pop())
            close: str = close_brackets.index(bracket)
            is_balanced = open == close
        else:
            is_balanced = False
        ndx += 1

    return symbol_stack.is_empty() and is_balanced
