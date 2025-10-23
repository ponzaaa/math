from numbers.rational import RationalNumber


class ComplexNumber():
    def __init__(self, real, imaginary):
        # Check that the inputs are RationalNumbers
        if not isinstance(real, RationalNumber):
            raise TypeError('Real part must be a RationalNumber')
        if not isinstance(imaginary, RationalNumber):
            raise TypeError('Imaginary part must be a RationalNumber')
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        new_real = self.real.add(other.real)
        new_imaginary = self.imaginary.add(other.imaginary)
        return ComplexNumber(new_real, new_imaginary)

    def subtract(self, other):
        new_real = self.real.subtract(other.real)
        new_imaginary = self.imaginary.subtract(other.imaginary)
        return ComplexNumber(new_real, new_imaginary)

    def multiply(self, other):
        ac = self.real.multiply(other.real)
        bd = self.imaginary.multiply(other.imaginary)
        ad = self.real.multiply(other.imaginary)
        bc = self.imaginary.multiply(other.real)
        new_real = ac.subtract(bd)
        new_imaginary = ad.add(bc)
        return ComplexNumber(new_real, new_imaginary)

    def __repr__(self):
        return f"({self.real} + {self.imaginary}i)"