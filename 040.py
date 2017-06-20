string = "";
for i in range(1, 200000):
    string += str(i);

prod = 1;
for i in range(7):
    prod *= int(string[10**i-1]);

print(prod);
