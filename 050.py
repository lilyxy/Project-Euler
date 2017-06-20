def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);
    return primeslist

pl = primes(1000000);

length = len(pl);

rec = 20;
attempt = rec + 1;
total = 0;


#odd values
while 1:
    attempt += 2;
    
    testsum = 0;
    for i in range(rec):
        testsum += pl[i];
    if testsum > 1000000:
        break;
    
    for i in range(0, length - attempt):
        summ = 0;
        for j in range(attempt):
            summ += pl[i+j];
        if summ >= 1000000:
            break;
        if summ in pl:
            print(attempt, summ);
            rec = attempt;
            total = summ;
            break;

#even value

for i in range(rec+1, attempt, 2):
    for j in range(0, 1):
        summ = 0;
        for j in range(attempt):
            summ += pl[i+j];
        if summ >= 1000000:
            break;
        if summ in pl:
            print(attempt, summ);
            rec = attempt;
            total = summ;
            break;


print(rec, total);
            
#make more efficient;
    
        
