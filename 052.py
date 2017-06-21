i = 1;
found = 0
while not found:
    if len(str(i*6)) > len(str(i)):
        i = 10**len(str(i));
    mults = [];
    for j in range(1, 7):
        l = list(str(i*j));
        l.sort();
        mults.append("".join(l));
    mults = set(mults);
    if len(mults) == 1:
        found = 1;
        print(i);
    i+=1;
