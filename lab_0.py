from random import randint

n = int(input("n="))

A = [randint(1, 4) for i in range(n)]

print(A)

n1 = n2 = n3 = n4 = 0

for i in range(1, n):
    if A[i] == 1:
        n1 += 1
    elif A[i] == 2:
        n2 += 1
    elif A[i] == 3:
        n3 += 1
    elif A[i] == 4:
        n4 += 1

print(n1, n2, n3, n4)
print(n1 / n, n2 / n, n3 / n, n4 / n)
