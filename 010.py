l = 2000000

n = range(1, l+1);

for i in range(0, l):
    if n[i] == 1:
        continue;
    for j in range(2*n[i] - 1, l, n[i]):
        while n[j]%n[i] == 0:
            n[j] /= n[i];

#n = [x for x in n if x != 1];
n = filter(lambda x: x!= 1, n)

sum = 0;
for i in n:
    sum += i;
print sum

