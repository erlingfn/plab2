""" Module for the containers stack and queue """


class Container:
    """ Super class for the containers stack and queue """

    def __init__(self):
        self._items = []

    def size(self):
        """ Return number of _items in self._items """
        return len(self._items)

    def is_empty(self):
        """ Return true if a list is empty, false is not """
        return len(self._items) == 0

    def push(self, item):
        """ Add an item to the end of self._items """
        raise NotImplementedError

    def pop(self):
        """ Remove and return top element """
        raise NotImplementedError

    def peek(self):
        """ Return top element without removing it """
        raise NotImplementedError


class Queue(Container):
    """Implementation of queue datastructure"""

    def peek(self):
        assert not self.is_empty()
        return self._items[0]

    def pop(self):
        assert not self.is_empty()
        return self._items.pop(0)

    def push(self, item):
        self._items.append(item)


class Stack(Container):
    """ Implementation of stack datastructure """

    def peek(self):
        assert not self.is_empty()
        return self._items[-1]

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop(-1)
