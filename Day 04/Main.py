with open("cleaning.txt", "r") as input:
    pairs = input.readlines()

pairs = [pair.strip().split(',') for pair in pairs]

for i in range(len(pairs)):
    pairs[i][0] = pairs[i][0].split('-')
    pairs[i][1] = pairs[i][1].split('-')

    pairs[i][0][0] = int(pairs[i][0][0])
    pairs[i][1][0] = int(pairs[i][1][0])
    pairs[i][0][1] = int(pairs[i][0][1])
    pairs[i][1][1] = int(pairs[i][1][1])


result = 0

for pair in pairs:
    if (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]) or (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]):
        result += 1

print("Part 1:", result)

result = len(pairs)
for pair in pairs:
    if pair[0][1] < pair[1][0] or pair[1][1] < pair[0][0]:
        result -= 1

print("Part 2:", result)