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

print("\n--- Testing Gaussian Elimination ---")
print("Solving the system:")
print("  1x + 1y = 3")
print("  2x + 3y = 8")

# Create the augmented matrix: [[1, 1, | 3],
#                              [2, 3, | 8]]
system_matrix = Matrix([
    Vector([create_rational(1, 1), create_rational(1, 1), create_rational(3, 1)]),
    Vector([create_rational(2, 1), create_rational(3, 1), create_rational(8, 1)])
])

print(f"\nOriginal Matrix:\n{system_matrix}")

# Run the algorithm! This modifies the matrix in-place.
system_matrix.gaussian_elimination()

print(f"\nSolved Matrix (Reduced Row-Echelon Form):\n{system_matrix}")

# The expected output is:
# Matrix([
#   Vector(1, 0, 1)  <--- This means 1x + 0y = 1
#   Vector(0, 1, 2)  <--- This means 0x + 1y = 2
# ])

print("\n--- Testing Gaussian Elimination (3x3 System) ---")
print("Solving the system:")
print("  2x + 1y - 1z = 8")
print(" -3x - 1y + 2z = -11")
print(" -2x + 1y + 2z = -3")

# Create the augmented 3x4 matrix
huge_matrix = Matrix([
    Vector([create_rational(2, 1), create_rational(1, 1), create_rational(-1, 1), create_rational(8, 1)]),
    Vector([create_rational(-3, 1), create_rational(-1, 1), create_rational(2, 1), create_rational(-11, 1)]),
    Vector([create_rational(-2, 1), create_rational(1, 1), create_rational(2, 1), create_rational(-3, 1)])
])

print(f"\nOriginal 3x4 Matrix:\n{huge_matrix}")

# Run the algorithm!
huge_matrix.gaussian_elimination()

print(f"\nSolved 3x4 Matrix:\n{huge_matrix}")

# The expected output is:
# Matrix([
#   Vector(1, 0, 0, 2)  <--- x = 2
#   Vector(0, 1, 0, 3)  <--- y = 3
#   Vector(0, 0, 1, -1) <--- z = -1
# ])

print("\n--- Testing Gaussian Elimination (4x4 FRACTIONAL System) ---")
print("Solving the system:")
print("  2x + 1y + 1z + 1w = 1")
print("  1x + 2y + 1z + 1w = 2")
print("  1x + 1y + 2z + 1w = 3")
print("  1x + 1y + 1z + 2w = 4")

# Create the augmented 4x5 matrix
# We can use create_rational() to make this cleaner!
r1 = create_rational(1, 1)
r2 = create_rational(2, 1)
r3 = create_rational(3, 1)
r4 = create_rational(4, 1)

fractional_matrix = Matrix([
    Vector([r2, r1, r1, r1, r1]),
    Vector([r1, r2, r1, r1, r2]),
    Vector([r1, r1, r2, r1, r3]),
    Vector([r1, r1, r1, r2, r4])
])

print(f"\nOriginal 4x5 Matrix:\n{fractional_matrix}")

# Run the algorithm!
fractional_matrix.gaussian_elimination()

print(f"\nSolved 4x5 Matrix:\n{fractional_matrix}")

# The expected output is:
# Matrix([
#   Vector(1, 0, 0, 0, (-1/5))  <--- x = -1/5
#   Vector(0, 1, 0, 0, (1/5))   <--- y = 1/5
#   Vector(0, 0, 1, 0, (3/5))   <--- z = 3/5
#   Vector(0, 0, 0, 1, (7/5))   <--- w = 7/5
# ])

print("\n--- Testing Gaussian Elimination (5x5 MONSTER System) ---")
print("Solving the system... (this may take a moment!)")

# Create the augmented 5x6 matrix
r1 = create_rational(1, 1)
r2 = create_rational(2, 1)
r3 = create_rational(3, 1)
r4 = create_rational(4, 1)
r5 = create_rational(5, 1)
r6 = create_rational(6, 1)
r10 = create_rational(10, 1)
r15 = create_rational(15, 1)
r20 = create_rational(20, 1)
r35 = create_rational(35, 1)
r70 = create_rational(70, 1)
r126 = create_rational(126, 1)
r210 = create_rational(210, 1)


monster_matrix = Matrix([
    Vector([r1, r1, r1, r1, r1, r15]),
    Vector([r1, r2, r3, r4, r5, r35]),
    Vector([r1, r3, r6, r10, r15, r70]),
    Vector([r1, r4, r10, r20, r35, r126]),
    Vector([r1, r5, r15, r35, r70, r210])
])

print(f"\nOriginal 5x6 Matrix:\n{monster_matrix}")

# Run the algorithm!
monster_matrix.gaussian_elimination()

print(f"\nSolved 5x6 Matrix:\n{monster_matrix}")

# The expected output is:
# Matrix([
#   Vector(1, 0, 0, 0, 0, 1)  <--- x = 1
#   Vector(0, 1, 0, 0, 0, 2)  <--- y = 2
#   Vector(0, 0, 1, 0, 0, 3)  <--- z = 3
#   Vector(0, 0, 0, 1, 0, 4)  <--- w = 4
#   Vector(0, 0, 0, 0, 1, 5)  <--- u = 5
# ])

print("\n--- Testing Gaussian Elimination (10x10 HILBERT MATRIX) ---")
print("Building 10x10 system...")

# This will be a 10x10 system (10 equations, 10 variables)
N = 10
matrix_rows = []

# We'll solve for x = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# We need to figure out what the 'b' vector (the solution column) should be
# For this test, let's just make a simple 'b' vector
b_vector = [create_rational(1, 1)] + [create_rational(0, 1)] * (N - 1)

# Build the 10x11 augmented matrix
for i in range(N):
    row_components = []
    for j in range(N):
        # A Hilbert Matrix element is 1 / (i + j + 1)
        row_components.append(create_rational(1, i + j + 1))

    # Add the augmented 'b' vector part
    row_components.append(b_vector[i])

    # Add the completed row to our matrix
    matrix_rows.append(Vector(row_components))

final_boss_matrix = Matrix(matrix_rows)

print(
    f"\nOriginal 10x11 Matrix (first 2 rows):\n{final_boss_matrix.row_vectors[0]}\n{final_boss_matrix.row_vectors[1]}")

# Run the algorithm! This will take a *long* time.
print("\nSolving... this is the final test!")
final_boss_matrix.gaussian_elimination()

print(
    f"\nSolved 10x11 Matrix (first 3 rows):\n{final_boss_matrix.row_vectors[0]}\n{final_boss_matrix.row_vectors[1]}\n{final_boss_matrix.row_vectors[2]}")

print("\n--- ALL TESTS COMPLETE ---")