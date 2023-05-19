from Complex import Complex

def fromStrToComplex(s):
    try:
        return Complex(float(s), 0)
    except ValueError:
        im_str = ''
        re_str = ''
        flag = False
        for i in range(len(s)):
            if (s[i] != '+' and s[i] != '-') or i == 0:
                if flag:
                    im_str += s[i]
                else:
                    re_str += s[i]
            else:
                flag = True
                if s[i] == '-':
                    im_str += '-'
        return Complex(float(re_str), float(im_str[:-1]))

print('Express coefficients in a form of a+bi for complex numbers and in usual form for real numbers.')
print('Notice that you should write 1+1i instead of 1+i and 0+2i instead of 2i.')

A = fromStrToComplex(input('Type the coefficient A of the equation.\n'))
B = fromStrToComplex(input('Type the coefficient B of the equation.\n'))
C = fromStrToComplex(input('Type the coefficient C of the equation.\n'))

Discriminant = B * B - A * C * Complex(4, 0)
if Discriminant is float or Discriminant is int:
    Discriminant = Complex(Discriminant, 0)

if abs(Discriminant) < 10 ** (-6):
    print('Equation has the only solution', str(-B / A / 2))
else:
    x1 = (-B + Discriminant.SquareRoot()[0]) / (A * 2)
    x2 = (-B + Discriminant.SquareRoot()[1]) / (A * 2)
    print('Equation has two solutions', str(x1), 'and', str(x2))