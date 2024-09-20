print("======================================")
print("Derivative Calculator")
print("Please, respect the pattern")

print("1*x ^ [2]. That reads as x to the power of two, and such a polynomial has 2x^(1) as the answer.")

# Input as integers
a = int(input("Enter the number multiplying X (can be 1): "))
b = int(input("Enter the number dividing X (can be 1): "))
n = int(input("Enter the exponent of X (can be 1): "))

# Derivation: Using the power rule [x^(n) => n*x^(n-1)]
# Initial term is (a * x^n) / b
# The derivative will be (a * n * x^(n-1)) / b
if n == 1:
    derivative = f"{a}/{b}"  # If exponent is 1, derivative is a constant
else:
    derivative = f"{a * n}*x^{n - 1}/{b}"  # General case for exponent n

print(f"The derivative of the expression is: {derivative}")