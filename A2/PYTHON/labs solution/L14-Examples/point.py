class point(object):
    count=0
    '''A class for a simple 2-dimensional point.'''
    def __init__(self, new_x, new_y):
        'The constructor method.'
        self.x = new_x
        self.y = new_y
        point.count +=1

    def __repr__(self):
        return "point({}, {})".format(self.x, self.y)
    
    def distance(self, other):
        'Euclidean distance to another point.'
        dx, dy = self.x - other.x, self.y - other.y
        return (dx * dx + dy * dy) ** 0.5
