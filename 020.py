def factorial(n):
    prod = 1;
    for i in range(1, n+1):
        prod *= i;
    return prod;
print(sum(map(int, list(str(factorial(99))))));
