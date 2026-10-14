def flatten(L):
    """
    L: a list
    return: a copy of L, which is a flattened version of L
    """
    if len(L) == 0:
        return []
    elif type(L[0]) != list:
        if len(L) == 1:
            return L
        else:
            return [L[0]] + flatten(L[1:])
    else:
        return flatten(L[0]) + flatten(L[1:])

    # another way
    # result = []
    # for i in L:
    #     if type(i) == list:
    #         result.extend(flatten(i))
    #     else:
    #         result.append(i)
    # return result


print(flatten([[1, 4, [6], 2], [[[3], 2], 4, 5]]))

