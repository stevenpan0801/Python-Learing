def keys_with_value(aDict, target):
    """
    aDict : a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.

    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    list_output = []
    for key in aDict.keys():
        if aDict[key] == target:
            list_output.append(key)
    list_output.sort()
    return list_output

aDict = {1:2, 2:4, 5:2}
target = 2
print(keys_with_value(aDict, target))