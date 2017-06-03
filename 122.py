import time
start_time = time.time()

def min_expo(limit):
        
    tree = [[1, -1, 0, 0]]; #value, parent, depth, place
    count = 1;

    if limit <= 1:
        return 0;

    for node in tree:
        if node[0] * 2 < limit:
            tree.append([node[0]*2, node[3], node[2] + 1, count]);
            count += 1;
        elif node[0] * 2 == limit:
            return node[2] + 1;
        parent = node[1]; 
        while parent >= 0:
            if node[0] + tree[parent][0] < limit:
                tree.append([node[0] + tree[parent][0], node[3], node[2] + 1, count]);
                count +=1;
            elif node[0] + tree[parent][0] == limit:
                return node[2] + 1;
            parent = tree[parent][1];

sum = 0;    
for i in range(0, 201):
    sum+= min_expo(i);

print sum;
        
print("--- %s seconds ---" % (time.time() - start_time))

        
    








































