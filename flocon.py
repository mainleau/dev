import sys
import tkinter
from math import sqrt

class complex(complex):
    def __iter__(self):
        return iter([(self.real, self.imag)])

class Vector:
    def __init__(self, a, b):
        self.a = complex(*a)
        self.b = complex(*b)

    @property
    def middle(self):
        return complex((self.a + self.b) / 2)

    @property
    def coordinates(self):
        return complex(self.b - self.a)

    @property
    def magnitude(self):
        return abs(self.coordinates)

    def normalize(self):
        return complex(self.coordinates / self.magnitude)

def get_third_point_equilateral(a, b, direction):
    vector = Vector(a, b)
    height = sqrt(vector.magnitude**2 - vector.magnitude**2/4)
    c = complex(*direction) * height + vector.middle
    return c.real, c.imag


def flocon(canvas, a, b, direction, deepness, deepness_max=4):
    vector = Vector(a, b)
    nv = [*vector.normalize()][0]
    l = vector.magnitude

    v1 = vector.normalize() * vector.magnitude * 1/3
    v2 = vector.normalize() * vector.magnitude * 2/3

    c = complex(vector.a + v1)
    d = complex(vector.a + v2)

    e = get_third_point_equilateral(*c, *d, *direction)

    c, d = complex(c - direction), complex(d - direction)

    canvas.create_polygon([*c, *d, e], fill='white')

    if deepness == deepness_max:
        return

    flocon(canvas, a, *c, direction, deepness+1, deepness_max)

    flocon(canvas, *d, b, direction, deepness+1, deepness_max)

    vector = Vector(*c, e)
    v = Vector(*d, *vector.middle).normalize()
    flocon(canvas, *c, e, v, deepness+1, deepness_max)

    vector = Vector(e, *d)
    v = Vector(*c, *vector.middle).normalize()
    flocon(canvas, e, *d, v, deepness+1, deepness_max)

def main(argv):
    WINDOW_WIDTH = WINDOW_HEIGTH = 1000

    window = tkinter.Tk()
    window.title('Un flocon de neige')

    canvas = tkinter.Canvas(window,
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGTH,
        bg='dark blue'
    )

    deepness_max = 4
    if (len(argv) > 1):
        deepness_max = int(argv[1])
    
    vector = Vector((100, 270), (900, 270))

    a, b = *vector.a, *vector.b
    c = get_third_point_equilateral(a, b, [0, 1])

    canvas.create_polygon([a, b, c], fill='white')
    canvas.pack()
    
    direction = Vector(c, *vector.middle).normalize()
    flocon(canvas, a, b, direction, 0, deepness_max)

    direction = Vector(a, *vector.middle).normalize()
    flocon(canvas, b, c, direction, 0, deepness_max)

    direction = Vector(b, *vector.middle).normalize()
    flocon(canvas, c, a, direction, 0, deepness_max)

    window.mainloop()

if __name__ == "__main__":
    main(sys.argv)
