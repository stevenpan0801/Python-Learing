class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initialize an empty list
        """
        self.list = []

    def size(self):
        """
        Return the list of the container list
        """
        return len(self.list)

    def add(self, elem):
        """
        Add the elem to one of the end of the container list, keeping the end you add to consistent. Does not return anything
        """
        self.list.append(elem)

class Stack(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the container list is removed.
        Return the element removed or None if the queue contains no elements.
        """
        if self.size() > 0:
            return self.list.pop()
        else:
            return None
    