fills = [[1,0],[1,0]]#last_black, last_red

for i in range(2, 1000):
    black = sum(fills[i-1]);
    red = 0;
    for j in range(0, i-49):
        red += fills[j][0];
    fills.append([black, red]);
    if black + red > 1000000:
        print(i);
        break;
print(sum(fills[50]))
  
