def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);
    return primeslist

p = primes(1000000);

s = 0;

pd = ['2', '4', '6', '8', '0', '5']
    
for i in p:
    circular = 1;
    length = len(str(i))
    a = list(str(i));
    for d in pd:
        if d in a and length>1:
            #print(d, a);
            circular = 0;
            break;
    if not circular:
        continue;
    c = i
    for k in range(length-1):
        c = (c%10)*(10**(length-1)) + c//10;
        if c not in p:
            circular = 0;
            break;
            
    if circular:
        #print(i);
        s += 1;
print(s)
