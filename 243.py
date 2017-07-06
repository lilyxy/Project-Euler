def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);
    return primeslist

primeslist = primes(10000);

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

def resilience(n):
    tot = totient(n);
    return (tot)/(n-1);


curr = 60060;
rec = 10;
recnum = 10;
while 1:
    res = resilience(curr);
    if res < rec:
        #print(res, recnum - res, curr);
        recnum = curr;
        rec = res;
    if res < 15499.0/94744:
        print(curr)
        break;
    curr += 60060;

