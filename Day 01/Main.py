with open('food.txt', 'r') as file:
    portions = file.readlines()
portions = [x.strip() for x in portions]

calories = []

food = 0
for portion in portions:
    if portion == '':
        calories.append(food)
        food = 0
    else:
        food += int(portion)

calories.sort(reverse=True)

print (calories[0])
print (calories[0] + calories[1] + calories[2])