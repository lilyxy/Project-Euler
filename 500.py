
def primes(n):
    primeslist = [];
    ind = [1 for i in range(n+1)];
    for i in range(2, n+1):
        if ind[i] == 1:
            for j in range(i*2, n+1, i):
                ind[j] = 0;
            primeslist.append(i);
    return primeslist


a = primes(10000000);
apowers = [];
indicies = [];
listcount = 0;

#find how many lists needed
for i in range(10):
    if 2**(2**(i)) < 10000000:
        apowers.append([]);
        indicies.append(0);
        listcount += 1;

#populate lists with marginal products
apowers[0] = a;
for i in range(1, listcount):
    for p in a:
        nextval = p**(2**i)
        if nextval < 10000000:
            apowers[i].append(nextval);
        else:
            break;
    apowers[i].append(10000000 + 1); #to prevent out of index


#find minimal amounts of each prime;
count = 0;
while count < 500500:
    least = min(list(apowers[i][indicies[i]] for i in range(listcount)));
    for i in range(listcount):
        if apowers[i][indicies[i]] == least:
            indicies[i] += 1;
            count += 1;
            break;
#print(indicies, sum(indicies));

prod = 1;
for i in range(listcount):
    for j in range(indicies[i]):
        prod *= a[j]**(2**i);
        prod %= 500500507;


print(prod)

