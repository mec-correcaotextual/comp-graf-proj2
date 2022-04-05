import itertools


class Matrix:
    
    @staticmethod
    def dot_product(x, y):
        assert len(x) == len(y)
        return sum(x * y)
