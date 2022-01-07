# initialize dict for calculated values
values = dict()

FILE = "input.txt"
with open(FILE, 'r') as infile:
    arr = list(map(int, infile.readline().strip().split(',')))
arr.sort()

# initialize array values
current_num = 0
idx = 0

# loop over
while current_num < arr[len(arr) - 1]:
    cost = 0
    for i in arr:
        n = abs(current_num - i)
        cost += n*(n+1)//2
    values[current_num] = cost
    current_num += 1

shortest = values[arr[0]]
for key in values:
    if values[key] < shortest:
        shortest = values[key]

print(shortest)
