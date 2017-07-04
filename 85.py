closest = 10000;
area = 0;
for i in range(1, 2000):
    for j in range(1, 2000):
        rects = i*(i-1)*j*(j-1)//4;
        diff = abs(2000000 - rects);
        if diff < closest:
            closest = diff;
            area = (i-1)*(j-1);
            print(closest, rects, area, i, j);
