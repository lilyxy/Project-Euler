def first_bigger(b1, e1, b2, e2):
    return b1**(e1/e2) > b2;

file = open("base_exp.txt",'r');
nums = file.read().split("\n");
nums = list(list(map(int, i.split(","))) for i in nums);

index = 0
pair = nums[0]
for i in range(1000):
    if first_bigger(nums[i][0], nums[i][1], pair[0], pair[1]):
        pair = nums[i];
        index = i;
print(index + 1);
