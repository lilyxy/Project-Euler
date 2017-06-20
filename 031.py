count = 2; #for 200p and 2 100p
for c100 in range(0, 2): 
    for c50 in range(0, 5):
        for c20 in range(0, 11):
            for c10 in range(0, 21):
                for c5 in range(0, 41):
                    for c2 in range(0, 101):
                        if c100*100 + c50*50 + c20*20 + c10*10 + c5*5 + c2*2 <= 200:
                            count+=1;

print(count); 
