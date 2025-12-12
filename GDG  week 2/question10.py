def is_palindrome(x):
    return str(x) == str(x)[::-1]  #reversing the string 

print(is_palindrome(121))
