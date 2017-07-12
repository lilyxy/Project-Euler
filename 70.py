from collections import Counter

def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);
    return primeslist

primeslist = primes(50000);

minval = 20;
minn = 0;

length = len(primeslist);


for i in range(0, length):
    for j in range(i+1, length):
        p = primeslist[i];
        q = primeslist[j];
        t = (p - 1) * (q - 1);
        if p*q > 10**7:
            break;
        if Counter(list(str(t))) == Counter(list(str(p*q))):
            val = p*q/t;
            if val < minval:
                minval = val;
                minn = p*q;
                #print(p, q, p*q, minval);

print(minn);
