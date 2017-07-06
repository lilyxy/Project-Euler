e0 = [0, 1];
e1 = [0, 1];
for i in range(2, 31):
    e0.append(e0[i-1] + e1[i-1]);
    e1.append(e0[i-1]);

lose = 1 + e0[30] + e1[30] - 1 # + 1 for 2^30, - 1 for 0;
print (lose);

#Explanation: we only need to find n s.t. n xor 2n xor 3n = 0. for any substring
#01, we get 01 xor 10 xor 11 = 0; for any longer chains of 1, we get 0011...111
#xor 0111....110 xor 1011.....101 = 1111.....100. Therefore we only want numbers
#which have no consecutive 1s in binary form, and no more than 30 digits.
