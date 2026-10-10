def all_true(n, Lf):
    """
    n is an integer
    Lf is a list of functions that take in an integer and return a boolean

    Return True if each and every function in Lf returns True when called with n as a parameter. Otherwise, return False.
    """
    for f in Lf:
        if not f(n):
            return False
    return True