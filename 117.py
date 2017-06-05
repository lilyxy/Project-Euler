lim = 50;

tiles = [1, 1, 2, 4];
count = 3;
while count <= lim:
    tiles.append(tiles[count]+tiles[count - 1] + tiles[count - 2] + tiles[count - 3]);
    count += 1;
print tiles[lim];
