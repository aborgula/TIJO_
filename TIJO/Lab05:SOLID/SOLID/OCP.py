# Naruszona zasada OCP

class Figure:
    def draw(self):
        pass

class Square(Figure):
    def __init__(self, a):
        self.a = a

    def draw(self):
        for side in range(0, self.a):
            print(self.a * "o ")
        print()


class Triangle(Figure):
    def __init__(self, h):
        self.h = h

    def draw(self):
        for side in range(0, self.h):
            print(side * "o ")
        print()


class FigureDrawer:
    def draw(self, figure: Figure):
        figure.draw()


a = 5
h = 5

square = Square(a)
triangle = Triangle(h)

FigureDrawer().draw(square)
FigureDrawer().draw(triangle)