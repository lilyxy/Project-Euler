def period(n):

    denom = 1;
    past = [];
    mixed_subtracted = int(n**0.5);
    num = 1;
    
    while 1:
        denom = n - mixed_subtracted**2;
        denom //= num;
        integer_part = int((n**0.5 + mixed_subtracted)/denom);
        mixed_subtracted -= integer_part * denom;
        mixed_subtracted *= -1; 
        #print(integer_part, str(n)+"^0.5 - "+str(mixed_subtracted), denom);

        value = [integer_part, mixed_subtracted, denom];
        
        if value in past:
            return len(past) - past.index(value);
        else:
            past.append(value);

        denom, num = num, denom;

oddcount = 0;

for i in range(1, 10001):
    if not (i**0.5).is_integer():
        if period(i)%2 == 1:
            oddcount+=1;
            
print(oddcount);
        
