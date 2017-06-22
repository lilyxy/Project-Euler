#not submitted

rec = 0;
for i in range(1, 100):
    for j in range(1, 100):
        digs = list(map(int, list(str(i**j))));
        dsum = sum(digs);
        if dsum > rec:
            rec = dsum;
            #print(dsum, i, j, i**j);

print(rec);
