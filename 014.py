lim = 1000000

longest = 0;
number = 1;
for i in range (1, lim):
    count = 0;
    n = i;
    while n != 1:
        if n % 2 == 0:
            n /= 2;
        else:
            n = 3*n + 1;
        count+= 1;
    if count > longest:
        longest = count;
        number = i;
        print longest, number

print longest, number
