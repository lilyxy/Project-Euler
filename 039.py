ind = 1;
rec = 0;
for i in range(1, 1000):
    sol = 0;
    for a in range(1, i//3 + 1):
        for b in range(a, i//2 + 1):
            c = i - a - b;
            if c < b:
                break;
            if a**2 + b**2 == c**2:
                sol += 1;
    if sol > rec:
        rec = sol;
        ind = i;
print(rec, ind);
