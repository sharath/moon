import numpy as np


class Predictor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def lagrange_interpolate(self, px):
        # compute barycentric weights
        w = np.zeros((1, len(self.x)))
        for i in range(len(self.x)):
            prod = np.float64(1)
            for j in self.x:
                if self.x[i] != j:
                    prod *= self.x[j] - self.x[i]
            w[i] = 1.0/prod
        # evaluation at px
        pxn = 0
        pxd = 0
        for i in range(len(self.x)):
            pxn += (w[i] * self.y[i]) / (px - (self.x[i]))
            pxd += (w[i]) / (px - (self.x[i]))
        return pxn / pxd
