with open("yell.txt", "r") as input:
    monkeys = input.readlines()

monkeys = [monkey.strip() for monkey in monkeys]
monkeys = [monkey.split(": ") for monkey in monkeys]


yell = {}

for monkey in monkeys:
    try:
        yell.update({monkey[0] : int(monkey[1])})
    except:
        yell.update({monkey[0] : monkey[1].split(" ")})


def evaluate_monkey(monkey, dict):
    if type(dict[monkey]) == int:
        return dict[monkey]
    left = evaluate_monkey(dict[monkey][0], dict)
    right = evaluate_monkey(dict[monkey][2], dict)
    if dict[monkey][1] == "+":
        return left + right
    if dict[monkey][1] == "-":
        return left - right
    if dict[monkey][1] == "*":
        return left * right
    if dict[monkey][1] == "/":
        return left // right
    
print(evaluate_monkey("root", yell))

yell.pop("humn")
yell["root"][1] = "="

def is_humn_here(monkey: str, dict) -> bool:
    if monkey == "humn":
        return True
    if type(dict[monkey]) == int:
        return False
    return is_humn_here(dict[monkey][0], dict) or is_humn_here(dict[monkey][2], dict)

def evaluate_humn(monkey, dict, expected_value):
    if monkey == "humn":
        return expected_value

    is_left = is_humn_here(dict[monkey][0], dict)
    if is_left:
        known_value = evaluate_monkey(dict[monkey][2], dict)
    else:
        known_value = evaluate_monkey(dict[monkey][0], dict)

    if dict[monkey][1] == "+":    
        new_expected_value = expected_value - known_value
    if dict[monkey][1] == "-":
        if is_left:
            new_expected_value = known_value + expected_value
        else:
            new_expected_value = known_value - expected_value
    if dict[monkey][1] == "*":
        new_expected_value = expected_value // known_value
    if dict[monkey][1] == "/":
        if is_left:
            new_expected_value = known_value * expected_value
        else:
            new_expected_value = known_value // expected_value

    if is_left:
        return evaluate_humn(dict[monkey][0], dict, new_expected_value)
    else:
        return evaluate_humn(dict[monkey][2], dict, new_expected_value)


if is_humn_here(yell["root"][0], yell):
    starting_expected_value = evaluate_monkey(yell["root"][2], yell)
    human = evaluate_humn(yell["root"][0], yell, starting_expected_value)
else:
    starting_expected_value = evaluate_monkey(yell["root"][0], yell)
    human = evaluate_humn(yell["root"][2], yell, starting_expected_value)

print(human)