import math

class QuadraticEquation:
    def __init__(self, a: float, b:float, c:float):
        if a==0:
            raise ValueError("a nie moze być zerem")
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        delta = self.b ** 2 - 4 * self.a * self.c

        if delta > 0:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return x1, x2
        elif delta == 0:
            x = -self.b / (2*self.a)
            return x
        else:
            return None