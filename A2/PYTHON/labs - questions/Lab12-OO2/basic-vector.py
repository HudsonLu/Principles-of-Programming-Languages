class vector(object):
    '''A class that represents a simple vector in 0 or more dimensions.'''
    def __init__(self, comp=[]):
        self.components = comp
        self.size = len(comp)

    def __repr__(self):
        vector_info = "vector("
        if len(self.components) > 0:
            vector_info += str(self.components) #create a string from list
        return (vector_info + ')')
