# Add these imports to main.py
from numbers.complex import ComplexNumber
from calculus.trascendentals import create_exp_poly, create_cos_poly, create_sin_poly
from numbers.rational import create_rational

# Add this test block to the end of main.py
print("\n--- Testing Euler's Identity ---")
N_TERMS = 5  # How many terms to use in our approximations

print(f"Using {N_TERMS} terms for Taylor series approximations...")

# Create our polynomial approximations
exp_poly = create_exp_poly(N_TERMS)
sin_poly = create_sin_poly(N_TERMS)
cos_poly = create_cos_poly(N_TERMS)

# Define theta = pi/4 (approx 314/400) and i
theta = create_rational(314, 400) # An approximation for pi/4
i_imag = create_rational(1, 1)
zero_real = create_rational(0, 1)
i = ComplexNumber(zero_real, i_imag)  # Represents 'i'

# Calculate the input for e^(i*theta)
i_theta = i.multiply(ComplexNumber(theta, zero_real))
print(f"Input i*theta = {i_theta}")

# --- Calculate e^(i*theta) ---
e_i_theta = exp_poly.evaluate(i_theta)
print(f"e^(i*theta) approx = {e_i_theta}")

# --- Calculate cos(theta) + i*sin(theta) ---
cos_theta = cos_poly.evaluate(theta)
sin_theta = sin_poly.evaluate(theta)
cos_plus_i_sin = ComplexNumber(cos_theta, sin_theta)
print(f"cos(theta) + i*sin(theta) approx = {cos_plus_i_sin}")

print("\nAre the real and imaginary parts close? (Euler's Identity)")


