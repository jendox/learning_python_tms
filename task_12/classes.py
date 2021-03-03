class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Figure:
    @property
    def perimeter(self):
        raise NotImplemented
    @property
    def area(self):
        raise NotImplemented
    def side_size(self, x1, x2, y1, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

class Circle(Figure):
    def __init__(self, centre, r):
        self._centre = centre
        self._r = r
    @property
    def perimeter(self):
        return 2*3.14*self._r
    @property
    def area(self):
        return 3.14*self._r**2

class Triangle(Figure):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._ab = Figure.side_size(self, self._a.x, self._b.x, self._a.y, self._b.y)
        self._ac = Figure.side_size(self, self._a.x, self._c.x, self._a.y, self._c.y)
        self._bc = Figure.side_size(self, self._b.x, self._c.x, self._b.y, self._c.y)
    @property
    def perimeter(self):
        return self._ab + self._ac + self._bc
    @property
    def area(self):
        s = abs((self._b.x - self._a.x)*(self._c.y - self._a.y) - (self._c.x - self._a.x)*(self._b.y - self._a.y))/2
        return s

class Square(Figure):
    def __init__(self, a, b):
        self._a = a
        self._b = b
        self._ab = Figure.side_size(self, self._a.x, self._b.x, self._a.y, self._b.y)

    @property
    def perimeter(self):
        return self._ab*4
    @property
    def area(self):
        return self._ab**2