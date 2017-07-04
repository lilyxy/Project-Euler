def gcd(a,b):
    if a == 0:
        return b;
    else:
        return gcd(b%a, a);

prev = 21;
i = 120;
found = 0;
while not found:
    approxblue = max(int(i/(2**0.5)), 2);
    denom = i * (i - 1);
    blue = approxblue + 1
    num = blue * (blue - 1);
    gcd1 = gcd(blue, i);
    if gcd1 == 1:
        i+=1;
        continue;
    frac1 = [blue//gcd1, i//gcd1];
    gcd2 = gcd(blue - 1, i - 1);
    if gcd2 == 1:
        i+=1;
        continue;
    frac2 = [(blue - 1)//gcd2, (i - 1)//gcd2];
    frac3 = [frac1[0]*frac2[0], frac1[1]*frac2[1]];
    if frac3[0] == gcd(frac3[0], frac3[1]):
        #print(i, blue, i/prev);
        if i > 10**12:
            print(blue);
            break;
        prev, i = i, i*i/prev;
        i = int(i);
        
    else:
        i+=1;
    
#solutions for total roughly had ratio of 5.828 
