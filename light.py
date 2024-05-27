import numpy as np

class Light():

    def __init__(self, point) -> None:
        self.point = point
        self.i_s = np.array([1.0, 1.0, 1.0]) # rgb
        self.i_d = np.array([1.0, 1.0, 1.0]) # rgb
        self.i_a = np.array([0.8, 0.0, 0.8]) # rgb
        pass

