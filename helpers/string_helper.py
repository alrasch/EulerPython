__author__ = 'Aleks'


def is_palindrome(string):
    for i in range(0, len(string)-1):
        if not string[i] == string[len(string)-1-i]:
            return False
    return True