def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);
    return primeslist


def pundit_divis(n):
    if n%2 == 0 or n%5 == 0:
        return 0;
    if n == 3:
        return 3;
    m = n - 1
    for i in range(1, n//2+1):
        if m%i == 0:
            if int("1"*i)%n == 0:
                return i;
    return m;
            
            
    
primelist = primes(100000);
print("generated primes");

summ = 0;

for i in primelist:
    p = pundit_divis(i);
    if i > 5:
        if p%5 == 0:
            while p%5 == 0:
                p//= 5;
        if p%2 == 0:
            while p%2 == 0:
                p//= 2;
    if p == 1:
        print(i, pundit_divis(i));
    else:
        summ += i;



print(summ);
