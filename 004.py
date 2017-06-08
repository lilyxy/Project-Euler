largest = 0;
for i in range(100, 1000):
    for j in range(i, 1000):
        a = str(i*j);
        if a[::-1] == a and i*j > 900000:
            print a;

