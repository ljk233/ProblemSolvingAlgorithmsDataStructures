
"""
Problem Solving with Algorithms and Data Structures
===================================================
Implementation of the Stack Abstract Data Type.

"A stack (sometimes called a “push-down stack”) is an ordered
collection of items where the addition of new items and the removal of
existing items always takes place at the same end."

"This ordering principle is sometimes called LIFO, last-in first-out.
It provides an ordering based on length of time in the collection.
Newer items are near the top, while older items are near the base."
"""

# %%
from __future__ import annotations
from typing import Any


class Stack:
    """
    A stack is a data structure that stores a linear collection of
    items with access limited to a last-in first-out order.
    Adding and removing items is restricted to one end known as the top
    of the stack.
    An empty stack is one containing no items.

    """

    def __init__(self) -> None:
        """
        Creates and initialises an empty stack
        """
        self._items: list = list()

    def is_empty(self) -> bool:
        """
        Returns:
            `bool`: True if the stack is empty of objects, otherwise
            False
        """
        return self._items == list()

    def push(self, item: Any) -> None:
        """
        Adds a new item to the top of the stack.

        Args:
            item (Any): Item to be added to the top of the stack.
        """
        self._items.append(item)

    def pop(self) -> Any:
        """
        Removes the top item from the stack.
        The stack is modified.

        Returns
        -------
        Any
            item at the top of the stack, item is removed from the
            stack
        """
        return self._items.pop()

    def peek(self) -> Any:
        """
        Returns the top item from the stack but does not remove it.
        The stack is not modified.

        Returns
        -------
        Any
            next item that will be popped from the stack.
        """
        return self._items[self.size() - 1]

    def size(self) -> int:
        """
        Returns the number of items on the stack.

        Returns
        -------
        int
            Number of items in the stack
        """
        return len(self._items)

    # IMPLEMENTATION FOR `IN`, `LEN` and `REVERSE`

    def __len__(self) -> int:
        return len(self._items)

    def __reversed__(self) -> None:
        self._items = list(reversed(self._items))

    def __repr__(self) -> None:
        return "Stack()"
