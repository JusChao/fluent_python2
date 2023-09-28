from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


vector = Vector('3', '4')
vector1 = Vector('3', '4')
vector2 = Vector('3', '4')
# __repr__
print(vector)

# __abs__
print(abs(vector))

# __add__
print(vector1 + vector2)
