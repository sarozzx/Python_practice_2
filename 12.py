# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(str1):
    if str1==str1[::-1]:
        return True
    return False

str="ana"

print(is_palindrome(str))