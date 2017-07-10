def maxprod(n):
    prod = 1;
    for i in range(1, n+1):
        prod *= (2*i/(n+1))**i;
    return int(prod);

total = 0;
for i in range(2, 16):
    total += maxprod(i);
print(total);
