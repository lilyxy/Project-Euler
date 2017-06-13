#37

##find error later

def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;

            okay = 1;
            
            l = list(str(i));
            """
            alsobad = ['4', '6', '8', '9'];
            if (l[0] in alsobad) or (l[len(l)-1] in alsobad):
                okay = 0;
            """
            l = l[1:len(l)-1]
            bad = ['2','4','5','6','8','0']
            
            for b in bad:
                if b in l:
                    okay = 0;
            if okay or i < 10:
                primeslist.append(i);
    return primeslist


pl = primes(1000000);
summ = 0;

for i in pl:
    lc = i;
    rc = i;
    trunc = 1;
    if i < 10:
        trunc = 0;
    while lc != 0:
        if lc not in pl or rc not in pl:
            trunc = 0;
            break;
        lc = lc//10;
        length = len(str(rc));
        rc = rc%(10**(length-1));
    if trunc:

        summ += i;
print(summ);
