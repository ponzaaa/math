def decimal_to_binary(n):
    binary_list = []
    if n == 0:
        return [0]
    while n > 0:
        binary_list.insert(0, n % 2)
        n = n // 2
    return binary_list

def binary_to_decimal(binary_list):
    n = 0
    for i in range(1, len(binary_list) + 1):
        n += (2 ** (i-1)) * binary_list[-i]
    return n
