def AND_gate(A, B):
    if A == 1 and B == 1:
        return 1
    else:
        return 0

def XOR_gate(A, B):
    if (A == 1 and B == 0) or (A == 0 and B == 1):
        return 1
    else:
        return 0

def OR_gate(A, B):
    if A == 1 or B == 1:
        return 1
    else:
        return 0

def NOT_gate(A):
    if A == 1:
        return 0
    else:
        return 1