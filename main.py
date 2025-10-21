from set_theory.custom_set import CustomSet
from set_theory.relations import create_ordered_pair, is_function, get_range
from number_theory.divisibility import is_prime
from numbers.rational import RationalNumber


domain = CustomSet()
domain.add(1)
domain.add(2)
# Your __repr__ method will make this print nicely!
print(f"Domain set: {domain}")

codomain = CustomSet()
codomain.add('a')
codomain.add('b')
print(f"Codomain set: {codomain}")

pair_1_a = create_ordered_pair(1, 'a')
pair_2_b = create_ordered_pair(2, 'b')
pair_1_b = create_ordered_pair(1, 'b')

print(f"This is what the pair (1, 'a') looks like: {pair_1_a}")
print(f"This is what the pair (2, 'b') looks like: {pair_2_b}")

# --- Test 1: A valid function ---
# R1 = {(1, 'a'), (2, 'b')}
relation_is_function = CustomSet()
relation_is_function.add(pair_1_a)
relation_is_function.add(pair_2_b)

print(f"\nTesting relation {relation_is_function}")
print(f"Is this a function? {is_function(relation_is_function, domain)}")

# --- Test 2: Not a function (element 1 maps to two things) ---
# R2 = {(1, 'a'), (1, 'b')}
relation_not_function = CustomSet()
relation_not_function.add(pair_1_a)
relation_not_function.add(pair_1_b)

print(f"\nTesting relation {relation_not_function}")
print(f"Is this a function? {is_function(relation_not_function, domain)}")

# --- Test 3: Not a function (element 2 is missing) ---
# R3 = {(1, 'a')}
relation_missing_element = CustomSet()
relation_missing_element.add(pair_1_a)

print(f"\nTesting relation {relation_missing_element}")
print(f"Is this a function? {is_function(relation_missing_element, domain)}")

print("\n--- Testing Range ---")
print(f"For the valid function: {relation_is_function}")
function_range = get_range(relation_is_function)
print(f"The Range is: {function_range}") # Should print {'a', 'b'}

# Let's test a function where two inputs map to one output
# f = {(1, 'a'), (2, 'a')}
pair_2_a = create_ordered_pair(2, 'a')
function_many_to_one = CustomSet()
function_many_to_one.add(pair_1_a)
function_many_to_one.add(pair_2_a)

print(f"\nFor the many-to-one function: {function_many_to_one}")
print(f"Is it a function? {is_function(function_many_to_one, domain)}") # Should be True
many_to_one_range = get_range(function_many_to_one)
print(f"The Range is: {many_to_one_range}") # Should print just {'a'}

# Add this to the end of main.py
print("\n--- Testing is_prime ---")
print(f"Is 5 ([1, 0, 1]) prime? {is_prime([1, 0, 1])}") # True
print(f"Is 6 ([1, 1, 0]) prime? {is_prime([1, 1, 0])}") # False
print(f"Is 7 ([1, 1, 1]) prime? {is_prime([1, 1, 1])}") # True

# Add this to the end of main.py
print("\n--- Testing RationalNumber ---")

# --- Test 1: Creation and Simplification ---
# 2/4 should simplify to 1/2
num_a = RationalNumber([1, 0], [1, 0, 0]) # 2, 4
print(f"Creating 2/4: {num_a}") # Should print (1 / 10) i.e. 1/2

# --- Test 2: Addition (1/2 + 1/3 = 5/6) ---
num_b = RationalNumber([1], [1, 0]) # 1, 2
num_c = RationalNumber([1], [1, 1]) # 1, 3
sum_val = num_b.add(num_c)
print(f"1/2 + 1/3 = {sum_val}") # Should print (101 / 110) i.e. 5/6

# --- Test 3: Subtraction (1/2 - 1/3 = 1/6) ---
sub_val = num_b.subtract(num_c)
print(f"1/2 - 1/3 = {sub_val}") # Should print (1 / 110) i.e. 1/6

# --- Test 4: Multiplication (1/2 * 2/3 = 1/3) ---
num_d = RationalNumber([1, 0], [1, 1]) # 2, 3
mul_val = num_b.multiply(num_d)
print(f"1/2 * 2/3 = {mul_val}") # Should print (1 / 11) i.e. 1/3

# --- Test 5: Division (1/2 / 1/3 = 3/2) ---
div_val = num_b.divide(num_c)
print(f"1/2 / 1/3 = {div_val}") # Should print (11 / 10) i.e. 3/2