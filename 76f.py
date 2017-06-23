superlist = [[], [0, 1]];
for i in range(2, 101):

    sumways=[0];
    for init in range(1, i):
        end = min(i - init, init);
        count = sum(superlist[i-init][:end+1]);
        """
        count = 0;
        for j in range(min(init + 1, i - init)):
            count += superlist[i-init][j];
        """
        sumways.append(count);
    sumways.append(1);
    superlist.append(sumways);


#rewrite to just store largest

print(sum(superlist[100])-1)


