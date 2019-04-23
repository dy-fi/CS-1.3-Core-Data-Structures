#!python

from hashtable import HashTable

class Set(HashTable):

    def __init__(self, elements=None):
        self.table = HashTable()
        self.size = 0

        if elements:
            for i in elements:
                self.table.set(i, self.size)
                self.size += 1

    def __repr__(self):
        """return a string representation of this set"""
        return 'Set({!r})'.format(self.table.keys())
    
    def __iter__(self):
        """returns set iterator object"""
        self.index = 0
        return self

    def __next__(self):
        """returns the next element in the set iterator"""
        if self.index <= self.size:
            # if index = elements assigned size
            next = self.table.buckets.find(lambda key_value: key_value[1] == self.index)
            self.index += 1
            return next
    
    def __len__(self):
        return self.size

    def contains(self, element):
        """return a boolean indication whether element is in this set
        Best and worst case: O(1)"""
        return self.table.contains(element)

    def add(self, element):
        """add element to this set, if not present already
        Best and worst case: O(1)"""
        if not self.contains(element):
            self.size += 1
            self.table.set(element, self.size)
            
    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError
        Best case: O(1)
        worst case: O(n)"""
        if self.contains(element):
            self.size -= 1
        return self.table.delete(element)

    def union(self, other_set): 
        """return a new set that is the union of this set and other_set
        Best case: O(n)"""
        new_set = Set()
        # add keys from first set
        for key in self.table.keys():
            new_set.add(key)
        # add keys from second set
        # duplicates are taken care of by add()
        for key in other_set.table.keys():
            new_set.add(key)
        return new_set

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set
        Best and worst case: O(n)"""
        new_set = Set()
        for i in self.table.keys():
            # if found in both sets
            if other_set.contains(i):
                new_set.add(i)
        return new_set
    
    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set
        Best and worst case: O(n)"""
        new_set = Set()
        for i in self.table.keys():
            # if not in other_set
            if not other_set.contains(i):
                new_set.add(i)
        return new_set

    def is_subset(self, other_set):
        """return a boolean indicating whether other_set is a subset of this set
        Best and worst case: O(n)"""
        for i in other_set.table.keys():
            # if element is not in the other set
            if not self.contains(i):
                return False
        return True
    
