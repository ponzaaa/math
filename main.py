# --- Set Theory (Legacy) ---
# These tests show our original set-theory foundation
from set_theory.custom_set import CustomSet
from set_theory.relations import create_ordered_pair, is_function, get_range

# --- Number Theory ---
# We test is_prime, which needs bit-lists
from number_theory.divisibility import is_prime

# --- Converters & Creators (Our New "Dashboard") ---
# We use these to make our tests clean and readable
from utils.converters import decimal_to_binary
from numbers.rational import create_rational

# --- Linear Algebra ---
# The high-level classes we built
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix


print("--- Testing Set Theory ---")
domain = CustomSet()
domain.add(1)
domain.add(2)
print(f"Domain set: {domain}")

codomain = CustomSet()
codomain.add('a')
codomain.add('b')
print(f"Codomain set: {codomain}")

pair_1_a = create_ordered_pair(1, 'a')
pair_2_b = create_ordered_pair(2, 'b')
pair_1_b = create_ordered_pair(1, 'b')

# Test 1: A valid function
relation_is_function = CustomSet()
relation_is_function.add(pair_1_a)
relation_is_function.add(pair_2_b)
print(f"\nTesting relation {relation_is_function}")
print(f"Is this a function? {is_function(relation_is_function, domain)}") # Expected: True

# Test 2: Not a function (element 1 maps to two things)
relation_not_function = CustomSet()
relation_not_function.add(pair_1_a)
relation_not_function.add(pair_1_b)
print(f"\nTesting relation {relation_not_function}")
print(f"Is this a function? {is_function(relation_not_function, domain)}") # Expected: False

# Test 3: Get Range
print(f"\nThe Range of {relation_is_function} is: {get_range(relation_is_function)}") # Expected: {a, b}

# -----------------------------------------------------------------

print("\n--- Testing Number Theory (with converters) ---")
# Our is_prime function still uses the binary "engine"
print(f"Is 5 prime? {is_prime(decimal_to_binary(5))}") # Expected: True
print(f"Is 6 prime? {is_prime(decimal_to_binary(6))}") # Expected: False
print(f"Is 7 prime? {is_prime(decimal_to_binary(7))}") # Expected: True
print(f"Is 1 prime? {is_prime(decimal_to_binary(1))}") # Expected: False

# -----------------------------------------------------------------

print("\n--- Testing RationalNumber (with create_rational) ---")

# Test 1: Creation and Simplification
# 2/4 should simplify to 1/2
num_a = create_rational(2, 4)
print(f"Creating 2/4: {num_a}") # Expected: (1/2)

# Test 2: Creating from 0
num_zero = create_rational(0, 1)
print(f"Creating 0/1: {num_zero}") # Expected: 0

# Test 3: Addition (1/2 + 1/3 = 5/6)
num_b = create_rational(1, 2)
num_c = create_rational(1, 3)
sum_val = num_b.add(num_c)
print(f"1/2 + 1/3 = {sum_val}") # Expected: (5/6)

# Test 4: Subtraction (1/2 - 1/3 = 1/6)
sub_val = num_b.subtract(num_c)
print(f"1/2 - 1/3 = {sub_val}") # Expected: (1/6)

# Test 5: Multiplication (1/2 * 2/3 = 1/3)
num_d = create_rational(2, 3)
mul_val = num_b.multiply(num_d)
print(f"1/2 * 2/3 = {mul_val}") # Expected: (1/3)

# Test 6: Division (1/2 / 1/3 = 3/2)
div_val = num_b.divide(num_c)
print(f"1/2 / 1/3 = {div_val}") # Expected: (3/2)

# -----------------------------------------------------------------

print("\n--- Testing Linear Algebra (with create_rational) ---")

# --- 1. Vector Tests ---
print("\n--- Vector Tests ---")
# v1 = (1, 2)
v1 = Vector([create_rational(1, 1), create_rational(2, 1)])
# v2 = (3, 4)
v2 = Vector([create_rational(3, 1), create_rational(4, 1)])

print(f"v1 = {v1}")
print(f"v2 = {v2}")

# Test Vector Add: (1, 2) + (3, 4) = (4, 6)
v_add = v1.add(v2)
print(f"v1 + v2 = {v_add}") # Expected: Vector(4, 6)

# Test Vector Scale: 3 * (1, 2) = (3, 6)
scalar = create_rational(3, 1)
v_scale = v1.scale(scalar)
print(f"3 * v1 = {v_scale}") # Expected: Vector(3, 6)

# Test Vector Dot Product: (1, 2) • (3, 4) = 1*3 + 2*4 = 3 + 8 = 11
v_dot = v1.dot_product(v2)
print(f"v1 • v2 = {v_dot}") # Expected: 11

# --- 2. Matrix Tests ---
print("\n--- Matrix Tests ---")
# m1 = [[1, 2],
#       [3, 4]]
m1 = Matrix([
    Vector([create_rational(1, 1), create_rational(2, 1)]),
    Vector([create_rational(3, 1), create_rational(4, 1)])
])

# m2 = [[2, 0],
#       [1, 2]]
m2 = Matrix([
    Vector([create_rational(2, 1), create_rational(0, 1)]),
    Vector([create_rational(1, 1), create_rational(2, 1)])
])

print(f"m1 = \n{m1}")
print(f"m2 = \n{m2}")

# Test Matrix Add: m1 + m2 = [[3, 2], [4, 6]]
m_add = m1.add(m2)
print(f"m1 + m2 = \n{m_add}") # Expected: [[3, 2], [4, 6]]

# Test Matrix Multiply: m1 * m2
# Result: [[4, 4], [10, 8]]
m_mult = m1.multiply(m2)
print(f"m1 * m2 = \n{m_mult}") # Expected: [[4, 4], [10, 8]]