def primes(n):
    l = list(1 for i in range(n+1));
    primes = [];
    for i in range(2, n):
        if l[i]!=0:
            for k in range(2*i, n+1, i):
                l[k] = 0;
            primes.append(i);
    return primes;

bl = primes(2000);
print bl

def isprime(n):
    if n <= 1:
        return 0;
    for i in bl:
        if i>= n:
            return 1;
        if n%i == 0:
            return 0;
    return 1;



rec = 0;
for b in bl:
   
    for a in range(999, -999, -1):

        count = 0;
        for i in range(b):
            if isprime(i*i + i*a + b):
                count+=1;
            else:
                break;
        if count > rec:
            rec = count;
            print rec, a, b, a*b;

        







def gcd(a, b): #always with a <= b;
    if a == 0:
        return b;
    return gcd(b%a, a);

curr = 12;

while 1:
    numcount = 0;
    for i in range(1, curr):
        if gcd(i, curr) == 1:
            numcount += 1;
    if numcount*1.0/(curr-1) < 15499.0/94744:
        print curr
        break;
    curr += 6;

