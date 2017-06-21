def letterscore(name):
    letters =list(name);
    sum = 0;
    for i in letters:
        sum += ord(i) - ord('A') + 1
    return sum;

n_f = open("words.txt",'r');

trig = list(i*(i+1)//2 for i in range(1, 31));

arr=n_f.read().replace('"', "").split(",");
arr.sort();
count = 0;
l = len(arr);

for i in range(0, l):
    score = letterscore(arr[i]);
    if score in trig:
        count += 1;
        #print(arr[i], score);

print(count);
