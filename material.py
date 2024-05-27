

class Material():
    def __init__(self, k_a, k_s, k_d, n) -> None:
        self.k_a = k_a
        self.k_s = k_s
        self.k_d = k_d
        self.n = n
        

test1 = Material(k_a=0.2, k_d=0.25, k_s=0.75, n=10)