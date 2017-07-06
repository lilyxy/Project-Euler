count = 0;
for i in range(3, 250*27, 2):
    tn1 = 1;
    tn2 = 1;
    tn3 = 1;
    cycle = 0;
    divis = 0;
    triples = set();
    while not cycle and not divis:
        compress = str(tn1)+" "+str(tn2)+" "+str(tn3)
        if compress not in triples:
            triples.add(compress);
            tn1, tn2, tn3 = tn2, tn3, (tn1+tn2+tn3)%i;
            if tn3 == 0:
                divis = 1;
        else:
            cycle = 1;
            count += 1;
    if count == 124:
        break;
        print(i);
    
        
        
