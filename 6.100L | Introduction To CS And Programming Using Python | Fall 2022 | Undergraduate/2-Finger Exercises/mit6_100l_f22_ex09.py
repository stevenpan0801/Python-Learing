def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assume tA and tB are the same length.
    Returns the tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    #first element
    f1 = len(tA)

    #second element
    f2 = 0
    for i in range(len(tB)):
        f2 += tA[i] * tB[i]

    return (f1, f2)

tA = (1, 2, 3)
tB = (4, 5, 6)
print(dot_product(tA, tB))