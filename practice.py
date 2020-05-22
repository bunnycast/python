import math 
class Complex(object):
    def __init__(self, real, imaginary):
        self._real = real
        self._imaginary = imaginary
    def __add__(self, no):
        return Complex(self._real + no._real, self._imaginary + no._imaginary)
  
    def __sub__(self, no):
        return Complex(self._real - no._real, self._imaginary - no._imaginary)
        
    def __mul__(self, no):
        return Complex(self._real * no._real - self._imaginary * no._imaginary, self._real * no._real + self._imaginary * no._imaginary)

    def __truediv__(self, no):
        real_div = (self._real * no._real + self._imaginary * no._imaginary) / (no._real ** 2 + no._imaginary ** 2) 
        imag_div = (self._imaginary * no._real + self._real * no._imaginary) / (no._real ** 2 + no._imaginary ** 2) 
        return Complex(real_div, imag_div)
    
    def mod(self):
        return Complex(math.sqrt(self._real ** 2 + self._imaginary ** 2),0)

    def __str__(self):
        if self._imaginary == 0:
            result = "%.2f+0.00i" % (self._real)
        elif self._real == 0:
            if self._imaginary >= 0:
                result = "0.00+%.2fi" % (self._imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self._imaginary))
        elif self._imaginary > 0:
            result = "%.2f+%.2fi" % (self._real, self._imaginary)
        else:
            result = "%.2f-%.2fi" % (self._real, abs(self._imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')