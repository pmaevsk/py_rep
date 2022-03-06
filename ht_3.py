from math import pi


class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle*2 + side, 2)

    def __init__(self, d, h):
        self.d = d
        self.h = h
        self.area = self.make_area(d, h)


a = Cylinder(1, 2)
print(a.area)

print(a.make_area(2, 2))
