from .adders import full_adder
from .logic_gates import NOT_gate

def add_binary(A_list, B_list):
    A_list, B_list = zero_padding(A_list, B_list)
    result_list = []
    C_in = 0

    for i in range(1, len(A_list) + 1):
        A = A_list[-i]
        B = B_list[-i]
        S_col, C_col = full_adder(A, B, C_in)
        C_in = C_col
        result_list.insert(0, S_col)

    if C_in == 1:
        result_list.insert(0, C_in)

    return result_list

def subtract_binary(A_list, B_list):
    A_list, B_list = zero_padding(A_list, B_list)
    result = add_binary(A_list, two_complement(B_list))
    if len(result) > len(A_list):
        result.pop(0)
    return result

def multiply_binary(A_list, B_list):
    running_total = [0]
    shift_counter = 0
    for i in range(1, len(B_list) + 1):
        B_bit = B_list[-i]
        if B_bit == 1:
            shifted_A_list = shift_left(A_list, shift_counter)
            running_total = add_binary(shifted_A_list, running_total)
        shift_counter += 1
    return running_total

def divide_binary(A_list, B_list):
    quotient = []
    current_part = []
    for bit in A_list:
        current_part.append(bit)
        if is_less_or_equal(B_list, current_part):
            quotient.append(1)
            current_part = subtract_binary(current_part, B_list)
        else:
            quotient.append(0)
    return (quotient, current_part)


def invert_binary(bit_list):
    inverted_list = []
    for bit in bit_list:
        inverted_list.append(NOT_gate(bit))
    return inverted_list

def two_complement(bit_list):
    bit_list = invert_binary(bit_list)
    binary_one = [0] * (len(bit_list) - 1) + [1]
    bit_list = add_binary(bit_list, binary_one)
    return bit_list

def zero_padding(A_list, B_list):
    if len(A_list) < len(B_list):
        difference = len(B_list) - len(A_list)
        padding = [0] * difference
        A_list = padding + A_list
    elif len(B_list) < len(A_list):
        difference = len(A_list) - len(B_list)
        padding = [0] * difference
        B_list = padding + B_list
    return A_list, B_list

def shift_left(bit_list, num_places):
    bit_list = bit_list + ([0] * num_places)
    return bit_list

def is_less_or_equal(A_list, B_list):
    A_list, B_list = zero_padding(A_list, B_list)
    for i in range(0, len(A_list)):
        if B_list[i] > A_list[i]:
            return True
        elif A_list[i] > B_list[i]:
            return False
    return True


def trim_zeros(bit_list):
    if not bit_list:
        return [0]
    first_one_index = -1
    for i, bit in enumerate(bit_list):
        if bit == 1:
            first_one_index = i
            break
    if first_one_index == -1:
        return [0]
    else:
        return bit_list[first_one_index:]