roman = {'M':  1000,
         'CM': 900,
         'D':  500,
         'CD': 400,
         'C':  100,
         'XC': 90,
         'L':  50,
         'XL': 40,
         'X':  10,
         'IX': 9,
         'V':  5,
         'IV': 4,
         'I':  1}

roman_val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
roman_let = ['M', 'CM', 'D', 'CD','C','XC','L','XL','X','IX','V','IV','I']

def to_num(s):
    if len(s) == 0:
        return 0;
    elif len(s) == 1:
        return roman[s[0]]
    else:
        if roman[s[0]] < roman[s[1]]:
            return roman[s[1]] - roman[s[0]] + to_num(s[2:]);
        else:
            return roman[s[0]] + to_num(s[1:]);
    return 0;

def to_roman(n):
    string = ""
    length = len(roman_val);
    for i in range(0, length):
        if n >= roman_val[i]:
            while n >= roman_val[i]:
                string += roman_let[i];
                n -= roman_val[i];
    
    return string


n_f = open("roman.txt",'r');

trig = list(i*(i+1)//2 for i in range(1, 31));

arr=n_f.read().replace('\n', " ").split(" ");
count = 0;

for i in arr:
    number = to_num(i);
    efficient = to_roman(number);
    char_saved = len(i) - len(efficient);
    count += char_saved;
print(count)
