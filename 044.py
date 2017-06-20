def pen():
    penta = list(i*(3*i-1)//2 for i in range(1, 10001));
    for i in range(1, 1200):
        for j in range(0, 10000 - i):
            summ = penta[j] + penta[i+j]
            diff = penta[i+j] - penta[j]
            for k in range(int(((summ*2)//3)**0.5-1), int(((summ*2)//3)**0.5)+ 2):
                if k*(3*k-1)//2 == summ:
                    for l in range(int(((diff*2)//3)**0.5-1), int(((diff*2)//3)**0.5)+2):
                        if l*(3*l-1)//2 == diff:
                            print(diff, penta[i+j], penta[j], i);
                            return;
            """ 
            if (penta[j] + penta[i+j]) in penta:
                if (penta[i+j] - penta[j]) in penta:
                    print(penta[i+j], penta[j], i);
                    return;
            """
                
pen();
