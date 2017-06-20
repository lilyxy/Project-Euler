def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);
    return primeslist


def calc_rec_cycle(n):
    length = 1;
    curr = 9;
    while 1:
        if curr%n == 0:
            return length;
        else:
            length += 1;
            curr = 9 + 10*curr;
        

p = primes(1000);
p.remove(2);
p.remove(5);

rec = 0;
ind = 0;
for i in p:
    c = calc_rec_cycle(i);
    if c > rec:
        rec = c;
        ind = i;
        print(i, c);

print(ind);

        
