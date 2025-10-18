# main.py
from calculator import add_binary

# --- Let's test our add_binary function ---

# Test 1: 3 + 1 = 4
# 3 in binary is 11
# 1 in binary is 01
num1 = [1, 1]
num2 = [0, 1]
result1 = add_binary(num1, num2)
print(f"Test 1: {num1} + {num2} = {result1}") # Expected: [1, 0, 0]

# Test 2: 7 + 5 = 12
# 7 in binary is 111
# 5 in binary is 101 (which needs padding)
numA = [1, 1, 1]
numB = [1, 0, 1]
result2 = add_binary(numA, numB)
print(f"Test 2: {numA} + {numB} = {result2}") # Expected: [1, 1, 0, 0]

# Test 3: 1 + 1 = 2 (Tests the final carry)
# 1 in binary is 1
# 1 in binary is 1
numX = [1]
numY = [1]
result3 = add_binary(numX, numY)
print(f"Test 3: {numX} + {numY} = {result3}") # Expected: [1, 0]

# Test 4: 9 + 3 = 12 (Tests padding)
# 9 in binary is 1001
# 3 in binary is 11
numC = [1, 0, 0, 1]
numD = [1, 1]
result4 = add_binary(numC, numD)
print(f"Test 4: {numC} + {numD} = {result4}") # Expected: [1, 1, 0, 0]