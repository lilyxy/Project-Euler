s = 0;

for i in range(2, 1000000):
    fifth_dig_sum = sum(map(lambda x: x**5 ,map(int, list(str(i)))));
    if fifth_dig_sum == i:
        s += i;
print(s);
    
