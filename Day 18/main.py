with open("lava.txt", "r") as input:
    lava = input.readlines()

lava = [droplet.strip() for droplet in lava]
lava = [droplet.split(",") for droplet in lava]
lava = set([tuple([int(x) for x in droplet]) for droplet in lava])
surface = 0
for droplet in lava:
    x = droplet[0]
    y = droplet[1]
    z = droplet[2]
    if (x + 1, y, z) not in lava:
        surface += 1
    if (x - 1, y, z) not in lava:
        surface += 1
    if (x, y + 1, z) not in lava:
        surface += 1
    if (x, y - 1, z) not in lava:
        surface += 1
    if (x, y, z + 1) not in lava:
        surface += 1
    if (x, y, z - 1) not in lava:
        surface += 1
print(surface)


def fill_water(lava: set, start: int, end: int):
    water = set()
    Q = [(start, start, start)]
    while len(Q) != 0:
        n = Q.pop(0)
        if n not in lava and n not in water and n[0] >= start and n[0] <= end and n[1] >= start and n[1] <= end and n[2] >= start and n[2] <= end:
            water.add(n)
            Q.append((n[0] + 1, n[1], n[2]))
            Q.append((n[0] - 1, n[1], n[2]))
            Q.append((n[0], n[1] + 1, n[2]))
            Q.append((n[0], n[1] - 1, n[2]))
            Q.append((n[0], n[1], n[2] + 1))
            Q.append((n[0], n[1], n[2] - 1))
    return water

water = fill_water(lava, -5, 25)

surface = 0
for droplet in lava:
    x = droplet[0]
    y = droplet[1]
    z = droplet[2]
    if (x + 1, y, z) in water:
        surface += 1
    if (x - 1, y, z) in water:
        surface += 1
    if (x, y + 1, z) in water:
        surface += 1
    if (x, y - 1, z) in water:
        surface += 1
    if (x, y, z + 1) in water:
        surface += 1
    if (x, y, z - 1) in water:
        surface += 1
print(surface)