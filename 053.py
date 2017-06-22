#not submitted

def choose(n, r):
    if n < r:
        return 0;
    ans = 1;
    for i in range(r):
        ans *= n - i;
        ans //= i + 1;
    return ans;

count = 0;

for i in range(1, 101):
    for j in range(1, 101):
        if choose(i, j) > 1000000:
            count += 1;
            #print(i, j, choose(i, j))

print(count);
