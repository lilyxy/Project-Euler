def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);
    return primeslist

primeslist = primes(1000000);

def totient(n):
    total = 1;
    c = n;
    for p in primeslist:
        if c%p == 0:
            count = 0;
            while c%p == 0:
                c //= p;
                count += 1;
            total *= p**(count-1) * (p - 1)
        if c == 1:
            break;
    if c != 1:
        return n;
    return total;

maxval = 0;
maxn = 0;

for i in range(30, 1000001, 30):
    val = i/totient(i);
    if val > maxval:
        maxval = val;
        maxn = i;
print(maxn);
