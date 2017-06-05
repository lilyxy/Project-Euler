n = 20

def choose(n, k):
    a = 1;
    for i in range(n-k+1, n+1):
        a*=i;
    for i in range(1, k+1):
        a/=i;
    return a;

print choose(n*2,n)
