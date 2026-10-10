class Circle():
    def __init__(self, radius):
        """
        Initialize self with radius
        """
        self.r = radius

    def get_radius(self):
        """
        Return the radius of the circle
        """
        return self.r

    def __add__(self, c):
        """
        c is a Circle object
        return a new Circle object whose radius is the sum of self's and c's radius
        """
        return Circle(self.r + c.r)

    def __str__(self):
        """
        A Circle's string representation is the radius.
        """
        return str(self.r)