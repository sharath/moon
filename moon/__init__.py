import numpy as np


class Predictor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def lagrange_interpolate(self, px):
        w = []
        for i in range(len(self.x)):
            sum = np.float64(1)
            for j in range(len(self.x)):
                if i != j:
                    if self.x[i] != 0:
                        sum *= (self.x[i])
            w.append(np.float64(1.0 / sum))
        pxn = 0
        pxd = 0
        for i in range(len(self.x)):
            pxn += (w[i] * self.y[i]) / (px - (self.x[i]))
            pxd += (w[i]) / (px - (self.x[i]))
        return pxn / pxd
