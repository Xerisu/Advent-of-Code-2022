with open("trees.txt", "r") as input:
    trees = input.readlines()

trees = [line.strip() for line in trees]
trees = [[int(tree) for tree in line] for line in trees]
counting_trees = [[0 for _ in _] for _ in trees]

height = len(trees) - 1
width = len(trees[0]) - 1

for y in range(len(trees)):
    highest_left = -1
    highest_right = -1
    for x in range(len(trees[0])):
        if trees[y][x] > highest_left:
            counting_trees[y][x] = 1
            highest_left = trees[y][x]
        if trees[height - y][width - x] > highest_right:
            counting_trees[height - y][width - x] = 1
            highest_right = trees[height - y][width - x]

for x in range(len(trees[0])):
    highest_up = -1
    highest_down = -1
    for y in range(len(trees)):
        if trees[y][x] > highest_up:
            counting_trees[y][x] = 1
            highest_up = trees[y][x]
        if trees[height - y][width - x] > highest_down:
            counting_trees[height - y][width - x] = 1
            highest_down = trees[height - y][width - x]

result = 0
for line in counting_trees:
    for tree in line:
        result += tree

print(result)

optimal = 0
goodx = 0
goody = 0

for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[y]) - 1):
        up = 0
        counting_up = True
        down = 0
        counting_down = True
        for h in range(1, len(trees)):
            if y - h >= 0 and counting_up:
                up += 1
                if trees[y - h][x] >= trees[y][x]:
                    counting_up = False
            if y + h <= height and counting_down:
                down += 1
                if trees[y + h][x] >= trees[y][x]:
                    counting_down = False
        left = 0
        counting_left = True
        right = 0
        counting_right = True
        for w in range(1, len(trees[y])):
            if x - w >= 0 and counting_left:
                left += 1
                if trees[y][x - w] >= trees[y][x]:
                    counting_left = False
            if x + w <= width and counting_right:
                right += 1
                if trees[y][x + w] >= trees[y][x]:
                    counting_right = False
        
        view = up * down * left * right
        if view > optimal:
            optimal = view
print (optimal)