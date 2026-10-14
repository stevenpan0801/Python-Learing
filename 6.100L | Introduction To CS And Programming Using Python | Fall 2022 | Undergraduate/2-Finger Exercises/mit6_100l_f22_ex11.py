def remove_and_sort(Lin, k):
    """
    Lin is a list of ints
    k is an int >=0
    Mutates Lin to remove the first k elements in Lin and the sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    # Error code: L = L[...] creates a new list and rebinds the local variable.
    #             del L[...], L.append(), L.remove(), L.sort() mutate the original list.
    #             L is bounded to the same object with regard to Lin, the code bound Lin to another object but L is the same.
    # if k < len(Lin):
    #     Lin = Lin[k:]
    #     Lin.sort()
    # else:
    #     Lin = []
    if k < len(Lin):
        del(Lin[:k])
        Lin.sort()
    else:
        Lin.clear()


L = [1, 6, 3]
k = 1
remove_and_sort(L, k)
print(L)

k = 3
remove_and_sort(L, k)
print(L)