rec = 0;
for i in range(1, 10000):
    run = "";
    pand = 1;
    mult = 1;
    while len(run) < 9:
        run += str(mult*i);
        mult += 1;
    if len(run)>9:
        continue;
    l = list(run);
    l.sort();
    for j in range(0, 9):
        if int(l[j]) != j + 1:
            pand = 0;
            break;
    if pand:
        if int(run)>rec:
            print(i, run);
            rec = int(run);

print(rec)
