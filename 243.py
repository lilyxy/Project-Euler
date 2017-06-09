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
    curr += 1;

