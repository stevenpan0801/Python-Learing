def sum_str_lengths(l):
    """
    L is a non-empty list containing either:
    * string elements or
    * a non-empty sublist of string elements

    Returns the sum of the length of all strings in L and lengths of strings in the sublists of L.
    If L contains an element that is not a string or a list, or L's sublist contains an element that is not a string, raise a ValueError.
    """
    len_str = 0
    for elem1 in l:
        if type(elem1) == str:
            len_str += len(elem1)
        elif type(elem1) == list:
            for elem2 in elem1:
                if type(elem2) == str:
                    len_str += len(elem2)
                else:
                    return ValueError
        else:
            return ValueError
    return len_str

print(sum_str_lengths(["abcd", ["e", "fg"]]))
print(sum_str_lengths([12, ["e", "fg"]]))
print(sum_str_lengths(["abcd", ["3", "fg"]]))