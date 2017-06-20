def dist_factors(n):
    if n <= 1:
        return 0;
    count = 0;
    for i in range(2, n+1):
        if n%i == 0:
            count += 1;
            while n%i == 0:
                n//=i;
    return count;
last1 = 0;
last2 = 0;
last3 = 0;
i = 1;
while i>0:
    factors = dist_factors(i);
    if factors == 4:
        if last1 == last2 and last2 == last3 and last3 == 4:
            break;
        last3, last2, last1 = last2, last1, factors;
        i+=1;
    else:
        last1, last2, last3 = 0, 0, 0;
        i+=4;

print(i-3);
