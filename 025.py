#36

summ = 0;
for i in range(1, 1000000):
    s = str(i);
    if s == s[::-1]:
        b = bin(i);
        #print(b)
        sb = str(b)[2:];
        if sb == sb[::-1]:
            print(s, sb);
            summ += i;
print(summ);
