n = 20;
while 1:
    for i in range (2, 21):
        divis = 1;
        if n % i != 0:
            divis = 0;
            break;
    if divis == 1:
        print n;
        break;        
    n+=20;


