def is_palindromic(z):
    if list(str(z)) == list(str(z))[::-1]:
        return True
    else:
        return False