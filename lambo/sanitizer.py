import numpy as np


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
