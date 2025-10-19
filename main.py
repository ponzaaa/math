from set_theory.custom_set import CustomSet
from set_theory.relations import create_ordered_pair, is_function

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