def area(x1, y1, x2, y2, x3, y3):
    total = 0.5*(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2);
    if total < 0:
        total *= -1;
    return total;

def areadiff(a, b, c, d, e, f, p1, p2):
    total = area(a, b, c, d, e, f);
    total -= area(a, b, c, d, p1, p2);
    total -= area(a, b, e, f, p1, p2);
    total -= area(c, d, e, f, p1, p2);
    return total;

count = 0;
fil = open("triangles.txt",'r');
trig = fil.read().split("\n");
trig.remove("");
#for i in trig:
#    print i, "yo";
trig = list(map(int, a.split(",")) for a in trig);
for i in trig:
    diff = areadiff(i[0], i[1], i[2], i[3], i[4], i[5], 0, 0);
    if diff == 0:
        count+=1;

print count;
