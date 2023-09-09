class point(object):
    '''A class for a simple 2-dimensional point.'''
    tolerance = 1.0
    def __init__(self, new_x, new_y):
        'The constructor method.'
        self.x, self.y = new_x, new_y
    
    def copy(self):
        return point(self.x, self.y)

    def __repr__(self):
        return "point({}, {})".format(self.x, self.y)
    
    def distance(self, pt):
        'Euclidean distance to another point.'
        dx, dy = self.x - pt.x, self.y - pt.y
        return (dx * dx + dy * dy) ** 0.5
    
    def is_close_to(self,pt):
        temp = self.distance(pt)
        return (temp < point.tolerance)

    def __add__(self,p):
        temp = point(0,0)
        temp.x=self.x+p.x
        temp.y=self.y+p.y
        return(temp)

