#46


def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);
    return primeslist

squares2 = list(i*i*2 for i in range(1, 101));
primesl = primes(10000);

sums = [];
for i in squares2:
    for j in primesl:
        sums.append(i+j);

sums = set(sums)
for i in range(27, 100000, 2):
    if i not in sums:
        if i not in primesl:
            print(i);
            break;
        
