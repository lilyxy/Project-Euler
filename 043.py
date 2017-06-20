##only possible end digits, by hand calculation, were 357289 and 952867,
##starting from the 7th ending on 5 or 0, and generating 10 possibilities
##for the 8th and 9th with 5 - all cases beginning with 0 had repeat digits

import itertools;
pos = list(itertools.permutations(['1','0', '4', '6'], 4))
pos = list(int(''.join(i)) for i in pos)
sum = 0;
for i in pos:
    if i>1000:
        if i%2 == 0:
            if (i%100)%3 == 0:
                sum += int(str(i)+"357289")



pos = list(itertools.permutations(['1', '0', '4', '3'], 4))
pos = list(int(''.join(i)) for i in pos)

for i in pos:
    if i>1000:
        if i%2 == 0:
            if (i%100)%3 == 0:
                sum += int(str(i)+"952867")
print(sum);
