from arithmetic.calculator import is_equal, divide_binary, multiply_binary, add_binary, subtract_binary
from number_theory.divisibility import gcd
from utils.converters import binary_to_decimal, decimal_to_binary


def create_rational(p_int, q_int):
    """
    Creates a RationalNumber from two Python integers.
    """
    p_bits = decimal_to_binary(p_int)
    q_bits = decimal_to_binary(q_int)
    return RationalNumber(p_bits, q_bits)

class RationalNumber:
    def __init__(self, p, q):

        if is_equal(q, [0]):
            raise ValueError("You cannot divide by zero")
        greatest_common_divisor = gcd(p, q)
        self.p, _ = divide_binary(p, greatest_common_divisor)
        self.q, _ = divide_binary(q, greatest_common_divisor)

    def add(self, other_rational):
        numerator = add_binary(multiply_binary(self.p, other_rational.q),
                               multiply_binary(other_rational.p, self.q))
        denominator = multiply_binary(self.q, other_rational.q)
        return RationalNumber(numerator, denominator)

    def subtract(self, other_rational):
        nominator = subtract_binary(multiply_binary(self.p, other_rational.q),
                                    multiply_binary(other_rational.p, self.q))
        denominator = multiply_binary(self.q, other_rational.q)
        return RationalNumber(nominator, denominator)

    def multiply(self, other_rational):
        nominator = multiply_binary(self.p, other_rational.p)
        denominator = multiply_binary(self.q, other_rational.q)
        return RationalNumber(nominator, denominator)

    def divide(self, other_rational):
        nominator = multiply_binary(self.p, other_rational.q)
        denominator = multiply_binary(self.q, other_rational.p)
        return RationalNumber(nominator, denominator)

    def __repr__(self):
        p_decimal = binary_to_decimal(self.p)
        q_decimal = binary_to_decimal(self.q)

        if q_decimal == 1:
            return f"{p_decimal}"
        return f"({p_decimal}/{q_decimal})"