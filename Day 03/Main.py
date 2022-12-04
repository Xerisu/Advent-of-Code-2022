with open("rucksack.txt", "r") as input:
    items = input.readlines()

def getValue(error):
    if ord(error) >= ord('a') and ord(error) <= ord('z'):
        return ord(error) - ord('a') + 1
    else:
        return ord(error) - ord('A') + 27

rucksacks = [item.strip() for item in items]
items = [[set(item[0:len(item)//2]), set(item[len(item)//2:len(item)])] for item in rucksacks]
rucksacks = [set(item) for item in rucksacks]

result = 0
errors = ""
for rucksack in items:
    error = rucksack[0].intersection(rucksack[1]).pop()
    result += getValue(error)
    

print("Part 1:" + result)

# part 2
result = 0
for i in range(0,len(rucksacks),3):
    number = rucksacks[i].intersection(rucksacks[i+1], rucksacks[i+2]).pop()
    result += getValue(number)

print("Part 2:" + result)