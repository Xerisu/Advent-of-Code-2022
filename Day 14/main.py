import copy

with open("walls.txt", "r") as input:
    walls = input.readlines()

def falling_sand(sand: tuple, walls: set): # returns true if sand is still falling, false if it landed
    if (sand[0], sand[1] + 1) in walls: 
        if (sand[0] - 1, sand[1] + 1) not in walls:
            sand = (sand[0] - 1, sand[1] + 1)
            return sand, True
        if (sand[0] + 1, sand[1] + 1) not in walls:
            sand = (sand[0] + 1, sand[1] + 1)
            return sand, True
        walls.add(sand)
        return sand, False
    sand = (sand[0], sand[1] + 1)
    return sand, True

def falling_sand_with_floor(sand: tuple, walls: set, floor: int): # returns true if sand is still falling, false if it landed
    if (sand[0], sand[1] + 1) in walls: 
        if (sand[0] - 1, sand[1] + 1) not in walls:
            sand = (sand[0] - 1, sand[1] + 1)
            return sand, True
        if (sand[0] + 1, sand[1] + 1) not in walls:
            sand = (sand[0] + 1, sand[1] + 1)
            return sand, True
        walls.add(sand)
        return sand, False
    if sand[1] + 1 == floor:
        walls.add(sand)
        return sand, False
    sand = (sand[0], sand[1] + 1)
    return sand, True

walls = [x.strip().split("->") for x in walls]
walls = [[x.split(",") for x in wall] for wall in walls]
walls = [[[int(x) for x in y] for y in wall] for wall in walls]



rocks = set() # cause sand is, technicly, a rock. Just a very small one.

for wall in walls:
    for i in range(len(wall) - 1):
        if wall[i][0] == wall[i+1][0]:
            for j in range(min(wall[i][1],wall[i+1][1]), max(wall[i+1][1],wall[i][1]) + 1, 1):
                rocks.add((wall[i][0], j))
        else:
            for j in range(min(wall[i][0],wall[i+1][0]), max(wall[i+1][0],wall[i][0]) + 1, 1):
                rocks.add((j, wall[i][1]))

rocks2 = copy.deepcopy(rocks)
not_in_void = True
starting_walls = len(rocks)
while(not_in_void):
    sand = (500,0)
    keep_falling = True
    while(keep_falling == True):
        sand, keep_falling = falling_sand(sand, rocks)
        if sand[1] > 200:
            keep_falling = False
            not_in_void = False
    
print("Part 1:", len(rocks) - starting_walls)

max_y = 0
for wall in walls:
    for point in wall:
        max_y = max(max_y, point[1])

floor = max_y + 2

while((500,0) not in rocks2):
    sand = (500,0)
    keep_falling = True
    while(keep_falling == True):
        sand, keep_falling = falling_sand_with_floor(sand, rocks2, floor)

print("Part 2:", len(rocks2) - starting_walls)
