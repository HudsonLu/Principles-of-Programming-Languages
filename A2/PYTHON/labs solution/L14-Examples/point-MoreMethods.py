from math import sqrt

class point(object):
    '''A class for a simple 2-dimensional point.'''
    def __init__(self, new_x, new_y):
        'The constructor method.'
        self.x = new_x
        self.y = new_y

    def __eq__(self, pt):
        return self.x == pt.x and self.y == pt.y

    def __repr__(self):
        'String representation of a point.'
        return '({}, {})'.format(self.x, self.y)

    def copy(self):
        "Makes a copy of a point."
        return point(self.x, self.y)
        
    def distance(self, pt):
        'Euclidean distance between points.'
        dx, dy = self.x - pt.x, self.y - pt.y
        return sqrt(dx * dx + dy * dy)

