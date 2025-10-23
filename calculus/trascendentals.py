from calculus.polynomial import Polynomial
from numbers.rational import create_rational
from utils.tools import factorial

def create_exp_poly(n_terms):
    coefficients = []
    one = create_rational(1, 1)
    for i in range(0, n_terms):
        coefficients.append(one.divide(factorial(i)))
    coefficients.reverse()
    return Polynomial(coefficients)

def create_sin_poly(n_terms):
    coefficients = []
    one = create_rational(1, 1)
    zero = create_rational(0, 1)
    for i in range(0, n_terms):
        if i % 2 == 0:  # even
            coefficients.append(zero)
        else:  # odd
            if i % 4 == 3:
                coefficients.append(one.divide(factorial(i)).negate())
            else:
                coefficients.append(one.divide(factorial(i)))
    coefficients.reverse()
    return Polynomial(coefficients)

def create_cos_poly(n_terms):
    coefficients = []
    one = create_rational(1, 1)
    zero = create_rational(0, 1)
    for i in range(0, n_terms):
        if i % 2 == 1:  # odd
            coefficients.append(zero)
        else:  # odd
            if i % 4 == 2:
                coefficients.append(one.divide(factorial(i)).negate())
            else:
                coefficients.append(one.divide(factorial(i)))
    coefficients.reverse()
    return Polynomial(coefficients)
