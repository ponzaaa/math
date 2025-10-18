from adders import full_adder

def add_binary(A_list, B_list):
    if len(A_list) < len(B_list):
        difference = len(B_list) - len(A_list)
        padding = [0] * difference
        A_list = padding + A_list
    elif len(B_list) < len(A_list):
        difference = len(A_list) - len(B_list)
        padding = [0] * difference
        B_list = padding + B_list

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