#!python

class CircularBuffer(object):
    
    def __init__(self, iterable=None):
        """Initialize circular buffer and enqueue iterables"""
        self.list = list()
        self.front = 0
        if iterable:
            for i in iterable:
                self.enqueue(i)
    
    def __repr__(self):
        """Return a string representation of this circular buffer"""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        try:
            return self.list[0] == None
        except:
            return True

    def enqueue(self, item):
        """Insert the given item at the back of the circular buffer.
        Running time: O(1)"""
        self.list.append(list)

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) is_empty only needs to see head""" 
        if not self.is_empty():
            i = self.list[self.front]
            self.front += 1
            return i
        raise ValueError('Buffer is empty')

    
    