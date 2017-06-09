def letterscore(name):
    letters =list(name);
    sum = 0;
    for i in letters:
        sum += ord(i) - ord('A') + 1
    return sum;



n_f = open("names.txt",'r');



arr=n_f.read().replace('"', "").split(",");
arr.sort();
sum = 0;
l = len(arr);

for i in range(0, l):
    score = letterscore(arr[i]);
    #print(arr[i], score, i+1, (i+1)*score);
    sum += (i+1)*score;

print(sum);
