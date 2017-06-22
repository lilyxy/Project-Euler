powers = [0];
mods = [1]

init = 1;
last_ten = 2;

while init <= 7830457:
    powers.append(init);
    mods.append(last_ten);
    init *= 2;
    last_ten *= last_ten;
    last_ten %= 10**10

expo = 7830457;
length = len(powers);
prod = 1;

for i in range(len(powers)-1, -1, -1):
    if expo >= powers[i]:
        expo -= powers[i];
        prod *= mods[i];
prod *= 28433
prod %= 10**10
prod += 1;

print(expo, prod);


print()
