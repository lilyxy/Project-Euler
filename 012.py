import time
start_time = time.time()

def pfactors(n):
    for p in range(2, n+1):
        while n%p==0:
            yield p
            n=n//p
            if n==1: return

def process(n):
    l = list(pfactors(n));
    l2 = [];
    while l:
        f = l[0];
        l2.append([f, l.count(f)]);
        l = list(filter(lambda a: a != f, l));
    return l2;

def p12(n):
    l = process(n);
    if l[0][0] == 2:
        l[0][1] -= 1;
    prod = 1;
    for i in l:
        prod *= i[1] + 1;
    return prod;

last = 1;
last_fact = 1;
curr = 2;
while 1:
    curr_fact = p12(curr);
    if last_fact * curr_fact >= 500:
        print last, curr, last*curr//2
        break;
    last = curr;
    last_fact = curr_fact;
    curr += 1;

print "--- %s seconds ---" % (time.time() - start_time) 

