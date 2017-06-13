fact = [];
for i in range(0, 10):
    f = 1;
    for j in range(1, i+1):
        f *= j;
    fact.append(f);


tot = 0;
for i in range(3, 10000000):
    s = 0;
    dig = map(int, list(str(i)));
    for j in dig:
        s += fact[j];
    if s == i:
        print(i);
        tot += i;
print(tot);
