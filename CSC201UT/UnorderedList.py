"""
Python utilities used in CSC 201 at UT.
This file includes classes and methods related to the unordered list.
"""

from CSC201UT.Node import Node

class UnorderedList:
    """Defines an unordered list."""
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def add(self, item):
        temp = Node(item)
        temp._link = self._head

        if (self._head == None):
            self._tail = temp
        self._head = temp

        self._len += 1

    def append(self, item):
        temp = Node(item)
        
        if (self._head == None):
            self._head = temp
            self._tail = temp
        else:
            self._tail._link = temp
            self._tail = temp

        self._len += 1

    def pop(self, pos=None):
        if (pos == None):
            pos = self._len - 1
        current = self._head
        previous = None

        if (current == self._tail):
            self._head = None
            self._tail = None
        else:
            for i in range(pos):
                previous = current
                current = current._link

            # the item is at the head of the list
            if (previous == None):
                # just change the head
                self._head = current._link
            # otherwise, it's somewhere else in the list
            else:
                # route around the removed node
                previous._link = current._link

        # if the item was the tail, move the tail
        if (current._link == None):
            self._tail = previous

        self._len -= 1

        return current._data

    def is_empty(self):
        return (self._head == None)

    def size(self):
        return self._len

    def search(self, value):
        current = self._head

        while (current != None):
            if (current._data == value):
                return True
            current = current._link

        return False

    # removes an item from the list
    def remove(self, value):
        current = self._head
        previous = None

        # traverse the list
        while (current != None):
            # the value is found at current
            if (current._data == value):
                break
            # go to the next node
            previous = current
            current = current._link

        # the value wasn't found
        if (current == None):
            raise ValueError(f"{value} is not in the list!")

        # the item is at the head of the list
        if (previous == None):
            # just change the head
            self._head = current._link
        # otherwise, it's somewhere else in the list
        else:
            # route around the removed node
            previous._link = current._link

        # if the item was the tail, move the tail
        if (current._link == None):
            self._tail = previous

    def __str__(self):
        s = ""
        current = self._head

        # traverse the list
        while (current != None):
            s += f"{current._data} "
            current = current._link

        return s

    def __repr__(self):
        return self.__str__()

    def to_list(self):
        s = []
        current = self._head

        # traverse the list
        while (current != None):
            s.append(current._data)
            current = current._link

        return s

    def __iter__(self):
        return UnorderedListIterator(self._head)

class UnorderedListIterator:
    """Defines an iterator for the unordered list."""
    def __init__(self, head):
        self._curr = head

    def __iter__(self):
        return self

    def __next__(self):
        if (not self._curr):
            raise StopIteration
        value = self._curr._data
        self._curr = self._curr._link

        return value

