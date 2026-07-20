from math import sqrt, exp, cos, sin
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.norm = real ** 2 + imaginary ** 2
    def _force_complex_other(func):
        def wrapper(self, other):
            if isinstance(other, ComplexNumber) == False:
                other = ComplexNumber(other, 0)
            return func(self, other)
        return wrapper
    @_force_complex_other
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
    @_force_complex_other
    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(new_real, new_imaginary)
    @_force_complex_other
    def __radd__(self, other):
        return other + self
    
    @_force_complex_other
    def __mul__(self, other):
        a, b, c, d = self.real, self.imaginary, other.real, other.imaginary
        new_real = a * c - b * d
        new_imaginary = b * c + a * d
        return ComplexNumber(new_real, new_imaginary)
    @_force_complex_other
    def __rmul__(self, other):
        return other * self
    @_force_complex_other
    def __sub__(self, other):
        return self + ComplexNumber(-other.real, -other.imaginary)
    @_force_complex_other
    def __rsub__(self, other):
        return other - self
    def reciprocal(self):
        new_real = self.real / self.norm
        new_imaginary = -self.imaginary / self.norm
        return ComplexNumber(new_real, new_imaginary)
    @_force_complex_other
    def __truediv__(self, other):
        return self * other.reciprocal()
    @_force_complex_other
    def __rtruediv__(self, other):
        return other / self
        
    def __abs__(self):
        return sqrt(self.norm)
        
    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)
    def exp(self):
        a, b = self.real, self.imaginary
        new_real = exp(a) * cos(b)
        new_imaginary = exp(a) * sin(b)
        return ComplexNumber(new_real, new_imaginary)