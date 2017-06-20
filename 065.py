el = []
for i in range(1, 101):
    if i%3==0:
        el.append(2*i//3);  
    else:
        el.append(1);
el[0] =  2
el.reverse();
num = 1;
denom = 0;
for i in el:
    num, denom = denom + num*i, num
    #print(num, denom)
print(num)
ds = sum(list(map(int, list(str(num)))))
print(ds)
#print(el)

