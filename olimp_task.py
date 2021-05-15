import sympy as sy
A = [0]*12
for i in range(len(A)):
    A[i] = sy.Rational(1 / (i+1))
print(A)