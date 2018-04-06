import numpy as np
import scipy.interpolate

class Predictor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def lagrange_interpolate(self, px):
        return scipy.interpolate.BarycentricInterpolator(self.x, self.y)(px)


class Sanitizer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sanitize(self):
        sx = np.zeros((len(self.x)))
        sy = np.zeros((len(self.y)))
        for i in range(len(self.x)):
            sx[i] = np.float64(float(self.x[i]))
        for i in range(len(self.y)):
            sy[i] = np.float64(float(self.y[i]))
        return sx, sy
