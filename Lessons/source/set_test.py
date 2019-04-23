#!python

from set import Set
import unittest
import string

class SetTest(unittest.TestCase):
    
    def test_init(self):
        elements = ['A', 'B', 'C', 'D']
        s = Set(elements) # initialize with 'A', 'B', 'C', 'D'
        assert len(s) == 4
        assert s.size == 4

    def test_contains(self):
        s = Set()
        assert s.contains('a') is False
        elements = list(string.ascii_lowercase)
        s = Set(elements) # list containing all string.ascii_lowercase chars
        assert s.contains('a') # first entry
        assert s.contains('m') # middle entry
        assert s.contains('z') # last entry

    def test_add_and_remove(self):
        s = Set()
        s.add('I') # add first element
        assert len(s) == 1
        assert s.contains('I')
        s.add('K') # add second element
        assert len(s) == 2
        assert s.contains('K')
        s.add('I') # add first element again, should do nothing
        assert len(s) == 2
        assert s.contains('I')
        assert s.contains('K')
        # test remove
        s.remove('I') # remove first element
        assert s.contains('I') is False
        assert s.contains('K') 
        assert len(s) == 1 # size should be incremented down
        s.remove('K') # remove second element
        assert s.contains('K') is False
        assert len(s) == 0
    
    def test_remove_error(self):
        s = Set()
        s.add('I')
        s.remove('I')
        assert len(s) == 0
        with self.assertRaises(KeyError):
            s.remove('I') # element no longer exists
        with self.assertRaises(KeyError):
            s.remove('K') # element never existed
    
    def test_union(self):
        lowercase = list(string.ascii_lowercase)
        uppercase = list(string.ascii_uppercase)
        s = Set(lowercase) # ascii_lowercase
        other = Set(uppercase) # ascii_uppercase
        u = s.union(other)
        assert len(u) == 52 # no overlap between sets
        assert u.contains('a') # first element of s
        assert u.contains('A') # first element of other set
        assert u.contains('z') # last element of s
        assert u.contains('Z') # last element of other set
        # test union of completely overlapping sets
        other = Set(lowercase)
        u = s.union(other)
        assert len(u) == 26 # all elements of other are overlapping

    def test_intersection(self):
        lowercase = list(string.ascii_lowercase)
        uppercase = list(string.ascii_uppercase)
        s = Set(lowercase) # ascii_lowercase
        other = Set(uppercase) # ascii_uppercase
        i = s.intersection(other)
        assert len(i) == 0 # no overlap between sets
        assert i.contains('a') is False
        assert i.contains('Z') is False
        # test intersection of completely overlapping sets
        other = Set(lowercase)
        i = s.intersection(other)
        assert len(i) == 26
        assert i.contains('a') # first element
        assert i.contains('z') # last element

    def test_difference(self):
        lowercase = list(string.ascii_lowercase)
        uppercase = list(string.ascii_uppercase)
        s = Set(lowercase) # ascii_lowercase
        other = Set(uppercase) # ascii_uppercase
        d = s.difference(other)
        assert len(d) == 26 # difference should be equal to s
        assert d.contains('a')
        assert d.contains('A') is False # should not have any elements from other set
        # test difference of completely overlapping sets
        other = Set(lowercase)
        d = s.difference(other)
        assert len(d) == 0
        assert d.contains('a') is False # was first element
        assert d.contains('z') is False # was last element
    
    def test_is_subset(self):
        lowercase = list(string.ascii_lowercase)
        letters = list(string.ascii_letters)
        s = Set(letters) # ascii_letters
        other = Set(lowercase) # ascii_lowercase
        assert s.is_subset(other)

if __name__ == '__main__':
    unittest.main()
