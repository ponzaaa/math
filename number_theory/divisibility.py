from arithmetic.calculator import divide_binary, is_less_than, add_binary, is_equal


def is_divisible(a, b):
    quotient, remainder = divide_binary(a, b)
    return all(bit == 0 for bit in remainder)


def is_prime(a):
    if is_equal(a, [0]) or is_equal(a, [1]):
        return False

    i = [1, 0]  # start from 2
    while is_less_than(i, a):
        if is_divisible(a, i):
            return False
        i = add_binary(i, [1])
    return True


def gcd(a, b):
    # edge cases
    if is_equal(a, [0]):
        raise Exception('A is zero')
    elif is_equal(b, [0]):
        raise Exception('B is zero')
    elif is_equal(a, [1]) or is_equal(b, [1]):
        return [1]

    # base case
    if is_divisible(a, b):
        return b

    # Recursive step:
    _, remainder = divide_binary(a, b)
    return gcd(b, remainder)
