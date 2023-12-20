# write a function that checkes if a give string(case insensitive) is a palindrome.

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]