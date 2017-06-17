def sds(n):
    dig = list(map(int, list(str(n))));
    sdig = list(i*i for i in dig);
    return sum(sdig);

count = 0;
for i in range(1, 10000000):
    curr = i
    while 1:
        if curr == 1:
            break;
        elif curr == 89:
            count+=1;
            break;
        curr = sds(curr);
print(count);
