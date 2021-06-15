import statistics

X = [int(N) for N in input('Введите числа: ').split()]
print(X)
A = B = 0
for i in range(len(X)):
    if X[i] > 0:
        A += X[i]
        B += 1
print(A/B)
print(A)
X = ((abs(x) for x in X))
X = sorted(X, reverse=True)
print(X)


