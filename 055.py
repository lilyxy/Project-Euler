#55
count = 0;
for i in range(1, 10000):
    c = i;
    lychrel = 1;
    for j in range(50):
        c += int(str(c)[::-1]);
        if str(c) == str(c)[::-1]:
            lychrel = 0;
            break;
    if lychrel:
        count += 1;
print(count);
