fills = [[1,0],[1,0]]#last_black, last_red

for i in range(2, 51):
    black = sum(fills[i-1]);
    red = 0;
    for j in range(0, i-2):
        red += fills[j][0];
    fills.append([black, red]);

print(sum(fills[50]))
