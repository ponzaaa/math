from numbers.complex import ComplexNumber
from numbers.rational import create_rational, RationalNumber
from .function import Function

class Polynomial(Function):
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def evaluate(self, x):
        zero = create_rational(0, 1)
        if isinstance(x, ComplexNumber):
            result = ComplexNumber(zero, zero)
            for coefficient in self.coefficients:
                coefficient = ComplexNumber(coefficient, zero)
                result = result.multiply(x).add(coefficient)
        elif isinstance(x, RationalNumber):
            result = zero
            for coefficient in self.coefficients:
                result = result.multiply(x).add(coefficient)
        else:
            raise TypeError("Input x must be a RationalNumber or ComplexNumber")
        return result

    def differentiate(self):
        result_coefficients = []
        for i in range(len(self.coefficients) - 1):
            power = len(self.coefficients) - (i + 1)
            new_coef = self.coefficients[i].multiply(create_rational(power, 1))
            result_coefficients.append(new_coef)
        if not result_coefficients:
            return Polynomial([create_rational(0, 1)])
        return Polynomial(result_coefficients)

    def integrate(self, c=None):
        if c is None:
            c = create_rational(0, 1)
        result_coefficients = []
        for i in range(len(self.coefficients)):
            power = len(self.coefficients) - i
            new_coef = self.coefficients[i].divide(create_rational(power, 1))
            result_coefficients.append(new_coef)
        result_coefficients.append(c)
        return Polynomial(result_coefficients)