from copy import deepcopy

from arithmetic.calculator import is_equal, divide_binary, multiply_binary, add_binary, subtract_binary, \
    is_less_or_equal, is_less_than
from number_theory.divisibility import gcd
from utils.converters import binary_to_decimal, decimal_to_binary


def create_rational(p_int, q_int):
    """
    Creates a RationalNumber from two Python integers.
    """
    sign = 1
    if p_int < 0:
        sign *= -1
        p_int = abs(p_int)
    if q_int < 0:
        sign *= -1
        q_int = abs(q_int)
    if p_int == 0:
        sign = 1

    p_bits = decimal_to_binary(p_int)
    q_bits = decimal_to_binary(q_int)
    return RationalNumber(p_bits, q_bits, sign)


class RationalNumber:
    def __init__(self, p, q, sign=1):
        if is_equal(q, [0]):
            raise ValueError("You cannot divide by zero")
        if is_equal(p, [0]):
            self.p = [0]
            self.q = [1]
            self.sign = 1
            return
        greatest_common_divisor = gcd(p, q)
        self.p, _ = divide_binary(p, greatest_common_divisor)
        self.q, _ = divide_binary(q, greatest_common_divisor)
        self.sign = sign

    def add(self, other_rational):
        ad = multiply_binary(self.p, other_rational.q)
        cb = multiply_binary(other_rational.p, self.q)
        denominator = multiply_binary(self.q, other_rational.q)
        if self.sign * other_rational.sign == 1:
            numerator = add_binary(ad,cb)
            return RationalNumber(numerator, denominator, self.sign)
        else:
            if is_less_than(cb, ad):
                numerator = subtract_binary(ad,cb)
                return RationalNumber(numerator, denominator, self.sign)
            elif is_less_or_equal(ad, cb):
                numerator = subtract_binary(cb, ad)
                return RationalNumber(numerator, denominator, other_rational.sign)
            else:
                return RationalNumber([0], [1], 1)

    def subtract(self, other_rational):
        return self.add(other_rational.negate())

    def multiply(self, other_rational):
        nominator = multiply_binary(self.p, other_rational.p)
        denominator = multiply_binary(self.q, other_rational.q)
        sign = self.sign * other_rational.sign
        return RationalNumber(nominator, denominator, sign)

    def divide(self, other_rational):
        nominator = multiply_binary(self.p, other_rational.q)
        denominator = multiply_binary(self.q, other_rational.p)
        sign = self.sign * other_rational.sign
        return RationalNumber(nominator, denominator, sign)

    def is_zero(self):
        return is_equal(self.p, [0])

    def reciprocal(self):
        return RationalNumber([1], [1]).divide(self)

    def negate(self):
        return RationalNumber(self.p, self.q, -self.sign)

    def __repr__(self):
        p_decimal = binary_to_decimal(self.p)
        q_decimal = binary_to_decimal(self.q)
        sign_str = "-" if self.sign < 0 else ""
        if q_decimal == 1:
            return f"{sign_str}{p_decimal}"
        return f"({sign_str}{p_decimal}/{q_decimal})"