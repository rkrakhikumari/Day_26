def is_palindrome(word):
    return word ==word[::-1]

result = is_palindrome("radar")
print(result)
