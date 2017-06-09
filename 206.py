#32

pandprod = []

for i in range(1, 1000):
    for j in range(i+1, 10000):
        string = str(i*j) + str(i) + str(j)
        if len(string) > 9:
            break;
        elif len(string) < 9:
            continue;
        else:
            pand = 1;
            l = list(map(int, list(string)));
            l.sort();
            for k in range(0, 9):
                if l[k] != k+1:
                    pand = 0;
                    break;
            if pand:
                print(i, j, i*j)
                pandprod.append(i*j);

pandprod = set(pandprod);
print(sum(pandprod))
                
