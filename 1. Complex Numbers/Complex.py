import math

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class Complex:
    def __init__(self, Re, Im):
        self._Re = Re
        self._Im = Im

    def __abs__(self):
        return (self._Re ** 2 + self._Im ** 2) ** 0.5

    def norm(self):
        return self._Re ** 2 + self._Im ** 2

    def __neg__(self):
        return Complex(-self._Re, -self._Im)

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self._Re + other._Re, self._Im + other._Im)
        else:
            return Complex(self._Re + other, self._Im)

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self._Re - other._Re, self._Im - other._Im)
        else:
            return Complex(self._Re - other, self._Im)

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self._Re * other._Re - self._Im * other._Im, self._Re * other._Im + self._Im * other._Re)
        else:
            return Complex(self._Re * other, self._Im * other)


    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex((self._Re * other._Re + self._Im * other._Im) / other.norm(),
                           (- self._Re * other._Im + self._Im * other._Re) / other.norm())
        else:
            return Complex(self._Re / other, self._Im / other)

    def __str__(self):
        if self._Im == self._Re == 0:
            return '0'
        else:
            if self._Im == 1:
                imstr = '+i'
            elif self._Im == 0:
                imstr = ''
            elif self._Im == -1:
                imstr = '-i'
            elif self._Im > 0:
                imstr = '+' + str(self._Im) + 'i'
            elif self._Im < 0:
                imstr = str(self._Im) + 'i'

            if self._Re == 0:
                restr = ''
            else:
                restr = str(self._Re)
            comstr = restr + imstr
        return comstr if comstr[0] != '+' else comstr[1:]

    def SquareRoot(self):
        a = self._Re
        b = self._Im
        r = self.__abs__()
        if b != 0:
            root1 = Complex(((r + a) / 2) ** 0.5, sign(b) * ((r - a) / 2) ** 0.5)
            root2 = root1.__neg__()
            return [root1, root2]
        else:
            if a > 0:
                return [Complex(a ** 0.5, 0), Complex(- a ** 0.5, 0)]
            elif a < 0:
                return [Complex(0, (-a) ** 0.5), Complex(0, - (-a) ** 0.5)]

    def arg(self):
        r = abs(self)
        z = self / r
        angle = math.acos(z._Re)
        if z._Im > 0:
            return angle
        else:
            return -angle

    def __pow__(self, power, modulo=None):
        if abs(self) < 10 ** (-6):
            return 0
        else:
            angle = self.arg()
            r = abs(self)
            return  Complex(math.cos(angle * power), math.sin(angle * power)) * r ** power