import itertools;
n = 15;

def factorial(n):
    prod = 1;
    for i in range(2, n+1):
        prod *= i;
    return prod;

denom = factorial(n+1);
fif = list(i for i in range(1, n+1));

ways  = 1;
for i in range(1, (n - 1)//2 + 1):
    combs = list(itertools.combinations(fif, i));
    print(i);
    for j in combs:
        product = 1;
        for k in list(j):
            product *= k;
        ways+=product;

print(ways, denom, ways/denom, 1/(ways/denom));
