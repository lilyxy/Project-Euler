fib1 = 1;
fib2 = 1;
count = 1;
while len(str(fib1)) < 1000:
    count += 1;
    fib1, fib2 = fib2, fib1 + fib2;
print(count);
