def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);
    return primeslist

pl = primes(10000);
p = list(filter(lambda x: x>1000, pl));
length = len(p);
for i in range(0, length - 1):
    for j in range(i+1, length - 1):
        li = list(str(p[i]));
        lj = list(str(p[j]));
        li.sort();
        lj.sort();
        if li == lj:
            if 2*p[j] - p[i] in pl:
                lk = list(str(2*p[j]- p[i]));
                lk.sort();
                if lj == lk:
                    print(p[i], p[j], 2*p[j] - p[i]);
        
