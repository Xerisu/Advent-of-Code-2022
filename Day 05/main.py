import re

with open("boxes.txt", "r") as input:
    boxes = input.read().splitlines()

boxes = list(map(list, zip(*boxes)))
boxes = [[c for c in stack if c not in "[] "] for stack in boxes]
boxes = [x[::-1] for x in boxes if len(x) != 0]
boxesBut9001 = [[c for c in x] for x in boxes]


print(boxes)


pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")

with open("instructions.txt", "r") as input:
    for line in input.readlines():
        match = pattern.match(line)
        instruction = [int(x) for x in match.groups()]
        picker9001 = []
        for i in range(instruction[0]):
            boxes[instruction[2] - 1].append(boxes[instruction[1] - 1].pop()) #part 1

            picker9001.append(boxesBut9001[instruction[1] - 1].pop()) #part 2
            
        for j in range(instruction[0]):
            boxesBut9001[instruction[2] - 1].append(picker9001.pop()) #part 2
        
print("".join([box[-1] for box in boxes]))
print("".join([box[-1] for box in boxesBut9001]))