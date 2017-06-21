i = 1;
found = 0
while not found:
    found = 1;
    if len(str(i*6)) > len(str(i)):
        i = 10**len(str(i));
    mults = [];
    for j in range(1, 7):
        l = list(str(i*j));
        l.sort();
        mults.append(l);
    length = len(str(i));
    for a in range(1, 6):
        for b in range(0, length):
            if mults[a][b] != mults[0][b]
                found = 0;
    mults = set(mults);
    if len(mults) == 1:
        found = 1;
        print(i)
    i+=1;
