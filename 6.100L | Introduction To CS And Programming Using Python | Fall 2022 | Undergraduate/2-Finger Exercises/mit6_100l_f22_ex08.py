def same_chars(s1, s2):
    """
    s1 and s2 are both strings.
    Return boolean True is a character in s1 is also in s2, and vice versa.
    If a character only exists in one of s1 or s2, returns False.
    """
    # Flag = True
    # for char in s1:
    #     if char not in s2:
    #         Flag = False
    # for char in s2:
    #     if char not in s1:
    #         Flag = False
    # return Flag

    for char in s1:
        if char not in s2:
            return False
    for char in s2:
        if char not in s1:
            return False
    return True

print(same_chars('abc', 'cab'))
print(same_chars('abccc', 'caaab'))
print(same_chars('abcd', 'cabaa'))
print(same_chars('abcabc', 'cabz'))