#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index >= len(array):
        return None
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1

    while right >= left:
        half = (left + right) // 2
        if array[half] == item:
            return half
        elif array[half] > item:
            right = half - 1
        elif array[half] < item:
            left = half + 1
        else:
            return None


def binary_search_recursive(array, item, left=None, right=None):
    if left == None:
        left = 0
    if right == None:
        right = len(array) - 1
    if right >= left:
        half = (left + right) // 2

        if array[half] == item:
            return half
        elif array[half] > item:
            return binary_search_recursive(array, item, left, right - 1)
        elif array[half] < item:
            return binary_search_recursive(array, item, left + 1, right)
        return None
