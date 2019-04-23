#!python

import random

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    O(n)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern in text:
        return True
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    O(n)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern == '':
        return 0
        
    for i in range(len(text)):
        if text[i] == pattern[0]:
            if text[i:i + len(pattern)] == pattern:
                return i
    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    O(n)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    answer = []
    for i in range(len(text)):
        if text[i:i + len(pattern)] == pattern or pattern == '':
            answer.append(i)
    return answer
        
            

def get_dictionary():
    with open('usr/share/dict/words') as dictionary:
        return dictionary.read()

def generate_permutation(word):
    l = list(word)
    random.shuffle(l)
    return ''.join(l)

def generate_anagram(word):
    dictionary = get_dictionary()
    found = False
    while not found:
        new = generate_permutation(word)
        if new in dictionary:
            return new

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
