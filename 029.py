#41

import itertools
pands = list(itertools.permutations([1,2,3,4,5,6,7], 7));
primerpands = [];

def list_to_int(l):
    if not l:
        return 0;
    else:
        return l[0] + 10*list_to_int(l[1:]);


for i in pands:
    if i[0] == 1 or i[0] == 3 or i[0] == 7:
        primerpands.append(list_to_int(i));



def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);
    return primeslist

plist = primes(10000000)

rec = 0;
for i in primerpands:
    if i in plist:
        if i > rec:
            rec = i;
            print(i);
    
        
