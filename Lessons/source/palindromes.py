#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    text = text.lower()
    for i in text:
        if i not in string.ascii_lowercase:
            text = text.replace(i, "")
    txet = text[::-1]
    return text == txet #lmao


def is_palindrome_recursive(text, left=None, right=None):
    text = text.lower()
    if left == None:
        left = 0
    if right == None:
        right = len(text) - 1

    if left == right or left > right:
        return True
    if text[left] not in string.ascii_lowercase:
        return is_palindrome_recursive(text, left + 1, right)
    if text[right] not in string.ascii_lowercase:
        return is_palindrome_recursive(text, left, right - 1)
    elif text[right] == text[left]:
        return is_palindrome_recursive(text, left + 1, right - 1)
    return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
