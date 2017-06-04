l = 10001;

primes = [2];

n = 3;
count = 1;

while count < l:
    prime = 1;
    for p in primes:
        if n % p == 0:
            prime = 0;
            break;
    if prime:
        primes.append(n);
        count += 1;
    n += 2;

print primes[l-1];
print primes;
