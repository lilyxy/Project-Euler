def gcd(a, b):
    if a == 0:
        return b;
    else:
        return gcd(b%a, a);

num = 1;
denom = 1;

for a in range(10, 100):
    for b in range(a+1, 100):
        if a%10 != 0 and b%10 != 0:
            da = list(map(int, list(str(a))));
            db = list(map(int, list(str(b))));
            intersec = list(set(da).intersection(set(db)));
            if len(intersec) == 1:
                da.remove(intersec[0]);
                db.remove(intersec[0]);
                if a*db[0] == b*da[0]:
                    num*=da[0];
                    denom*=db[0];

num, denom = num//gcd(num, denom), denom//gcd(num, denom);
print(denom);
                    
 



                    
        
