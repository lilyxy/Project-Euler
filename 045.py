#45

trig = list(i*(i+1)//2 for i in range(1, 100000));
pent = list(i*(3*i - 1)//2 for i in range(1, 100000));
hexa = list(i*(2*i - 1) for i in range(1, 100000));

inter = set(trig).intersection(set(pent)).intersection(set(hexa));

print(list(inter)[2])
