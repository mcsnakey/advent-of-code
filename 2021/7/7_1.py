# initialize dict for calculated values
values = dict()

FILE = "input.txt"
with open(FILE, 'r') as infile:
    arr = list(map(int, infile.readline().strip().split(',')))
arr.sort()

# initialize array values
idx = 0
left_sum = 0
right_sum = sum(arr)

# loop over and shift sums based on double pointer problem
while idx < len(arr):
    current_num = arr[idx]
    shift = current_num
    r_idx = idx
    while r_idx + 1 < len(arr) and arr[r_idx+1] == current_num:
        r_idx += 1
        shift += current_num
    right_sum -= shift
    values[current_num] = abs(left_sum - current_num * idx) + (right_sum - current_num * (len(arr) - r_idx - 1))
    left_sum += shift
    idx = r_idx + 1

shortest = values[arr[0]]
for key in values:
    if values[key] < shortest:
        shortest = values[key]

print(shortest)
