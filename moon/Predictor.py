import scipy.interpolate


class Predictor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def lagrange_interpolate(self, px):
        return scipy.interpolate.BarycentricInterpolator(self.x, self.y)(px)
