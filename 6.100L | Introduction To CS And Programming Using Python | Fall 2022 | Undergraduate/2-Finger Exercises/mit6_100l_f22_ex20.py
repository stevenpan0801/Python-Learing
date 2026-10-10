class Container(object):
    """
    A Container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initialize an empty list
        """
        self.mylist = []

    def size(self):
        """
        Return the length of the container list
        """
        return len(self.mylist)

    def add(self, elem):
        """
        Add the elem to one end of the container list, keeping the end you add to consistent. Does not return anything
        """
        self.mylist.append(elem)

class Queue(Container):
    """
    A subclass of container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The oldest element in the container list is removed.
        Return the element removed or None if the stack contains no elements.
        """
        if self.size == 0:
            return None
        else:
            return self.mylist.pop(0)

l = Queue()
l.add(1)
l.add(2)
l.add(3)
print(l.size())
print(l.remove())