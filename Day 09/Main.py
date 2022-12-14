def sign(x):
    if x > 0:
        return 1
    if x == 0:
        return 0
    else:
        return -1

with open("rope.txt", "r") as input:
    instructions = input.readlines()

instructions = [i.strip().split(" ") for i in instructions]
for i in range(len(instructions)):
    instructions[i][1] = int(instructions[i][1])
# [x,y]
head = [0,0]
tail = [0,0]
tail_positions = {(0,0)}

for instruction in instructions:
    for i in range(instruction[1]):
        if instruction[0] == "U":
            head[1] += 1
        elif instruction[0] == "D":
            head[1] -= 1
        elif instruction[0] == "L":
            head[0] -= 1
        else: # "R"
            head[0] += 1
        
        if max(abs(head[0] - tail[0]), abs(head[1] - tail[1])) > 1:
            tail[0] += sign(head[0] - tail[0])
            tail[1] += sign(head[1] - tail[1])
            tail_positions.add(tuple(tail))

print(len(tail_positions))

rope = []
for i in range(10):
    rope.append([0,0])

rope_positions = {(0,0)}

for instruction in instructions:
    for i in range(instruction[1]):
        if instruction[0] == "U":
            rope[0][1] += 1
        elif instruction[0] == "D":
            rope[0][1] -= 1
        elif instruction[0] == "L":
            rope[0][0] -= 1
        else: # "R"
            rope[0][0] += 1
        for j in range(1, len(rope)):
            if max(abs(rope[j-1][0] - rope[j][0]), abs(rope[j-1][1] - rope[j][1])) > 1:
                rope[j][0] += sign(rope[j-1][0] - rope[j][0])
                rope[j][1] += sign(rope[j-1][1] - rope[j][1])
                if j == 9:            
                    rope_positions.add(tuple(rope[j]))


print(len(rope_positions))