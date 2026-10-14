class Circle(object):
    def __init__(self, radius):
        """
        Initialize a circle with radius.
        """
        self.r = radius

    def get_radius(self):
        """
        Return the radius of self.
        """
        return self.r

    def set_radius(self, radius):
        """
        radius is a number
        Change the radius of self to radius.
        """
        self.r = radius

    def get_area(self):
        """
        Return the area of self using pi = 3.14
        """
        return 3.14*self.r*self.r

    def equal(self, c):
        """
        c is a Circle object
        Return True if self and c have the same radius value.
        """
        return c.r == self.r

    def bigger(self, c):
        """
        c is a Circle object
        Return self or c, the Circle object with the bigger radius.
        """
        if c.r > self.r:
            return c
        elif c.r < self.r:
            return self
        else:
            raise ValueError