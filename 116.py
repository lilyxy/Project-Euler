colourings = [[],[],[1, 1, 2, 3],[1, 1, 1, 2],[1, 1, 1, 1]];
total = 0;
for c in range(2, 5):
    for i in range(4, 51):
        wayways = colourings[c][i-1] + colourings[c][i-c];
        colourings[c].append(wayways);
    total += colourings[c][50] - 1
print(total);
