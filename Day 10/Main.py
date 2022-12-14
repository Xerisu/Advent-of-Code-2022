def print_list(l):
    for row in l:
        for n in row:
            print(str(n) + " ", end="")
        print("")

with open("signal.txt", "r") as input:
    signal = input.readlines()

signal = [i.strip().split(" ") for i in signal]

for i in range(len(signal)):
    if signal[i][0] == "addx":
        signal[i][1] = int(signal[i][1])

x = 1
cycle = 1
result = 0
needed_cycles = [20,60,100,140,180,220]
for i in range(len(signal)):
    cycle += 1
    if cycle in needed_cycles:
        result += x*cycle
    if signal[i][0] == "addx":
        x += signal[i][1]
        cycle += 1
        if cycle in needed_cycles:
            result += x*cycle

print(result)
print(cycle)
screen = []
for y in range(6):
    screen.append([])
    for x in range(40):
        screen[y].append(".")


cycle = 0
pixel = 1
# y = cycle//40
# x = cycle%40
for i in range(len(signal)):
    if pixel == cycle%40 or pixel-1 == cycle%40 or pixel+1 == cycle%40:
        screen[cycle//40][cycle%40] = "#"
    cycle += 1
    if signal[i][0] == "addx":
        if pixel == cycle%40 or pixel-1 == cycle%40 or pixel+1 == cycle%40:
            screen[cycle//40][cycle%40] = "#"
        pixel += signal[i][1]
        cycle += 1

print(cycle)
print_list(screen)