from logic_gates import AND_gate, XOR_gate, OR_gate

def half_adder(A, B):
    S = XOR_gate(A, B)
    C = AND_gate(A, B)
    return (S, C)

def full_adder(A, B, C_in):
    S, C = half_adder(A, B)
    S2, C2 = half_adder(S, C_in)
    S_final = S2
    C_final = OR_gate(C, C2)
    return (S_final, C_final)
