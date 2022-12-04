with open("tictactoe.txt", "r") as input:
    strategy = input.readlines()

strategy = [x.strip().replace(" ", "") for x in strategy]


possible_results_part_1 = {
    "AX" : 3 + 1, 
    "AY" : 6 + 2,
    "AZ" : 0 + 3,
    "BX" : 0 + 1,
    "BY" : 3 + 2,
    "BZ" : 6 + 3,
    "CX" : 6 + 1,
    "CY" : 0 + 2,
    "CZ" : 3 + 3
}
print(possible_results_part_1)
score = 0
for match in strategy:
    score += possible_results_part_1[match]

print("Part 1:" + score)
# x lose y draw z win
# a rock b paper c sciccors
possible_results_part_2 = {
    "AX" : 0 + 3, 
    "AY" : 3 + 1,
    "AZ" : 6 + 2,
    "BX" : 0 + 1,
    "BY" : 3 + 2,
    "BZ" : 6 + 3,
    "CX" : 0 + 2,
    "CY" : 3 + 3,
    "CZ" : 6 + 1
}

print(possible_results_part_2)

score = 0
for match in strategy:
    score += possible_results_part_2[match]

print("Part 2:" + score)
