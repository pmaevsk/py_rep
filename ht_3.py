from math import pi


class Cylinder:
    @staticmethod
    def __make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle*2 + side, 2)

    def __init__(self, d, h):
        self.diam = d
        self.high = h
        self.__area = self.__make_area(d, h)

    def __setattr__(self, attr, value):
        if attr in ['diam', 'high', '_Cylinder__area']:
            self.__dict__[attr] = value
            if attr in ['diam', 'high']:
                try:
                    self.__dict__['_Cylinder__area'] = self.__make_area(
                        self.diam, self.high)
                except AttributeError:
                    pass
        else:
            raise AttributeError

    def get_area(self):
        return self.__dict__['_Cylinder__area']


a = Cylinder(1, 2)
print(a.get_area())
a.make_area(14, 5)
print(a.get_area())
a.diam = 3
a.high = 3
print(a.get_area())
a.make_area(3, 1)
print(a.get_area())
