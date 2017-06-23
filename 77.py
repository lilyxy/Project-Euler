def primes(n):
    primeslist = [];

    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);

    return primeslist

p = primes(100000);

superlist = [[], [], [1]];
for i in range(3, 101):

    sumways=[0 for k in range(i)];
    for init in p:
        if init >= i:
            break;
        end = min(i - init, init);
        count = sum(superlist[i-init][:end+1]);
        sumways[init] = count;
    if i in p:
        sumways.append(1);
    else:
        sumways.append(0);
    if sum(sumways) > 5000:
        print(i);
        break;
    superlist.append(sumways);



print(superlist[10])
