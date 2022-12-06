with open("message.txt", "r") as input:
    message = input.readline()

def isUnique(message):
    buffer = message[0]
    for i in range(1, len(message)):
        if message[i] in buffer:
            return False
        buffer += message[i]
    return True


for i in range(3, len(message)):
    part = message[i-3:i+1]
    if isUnique(part):
        print(part, i+1)
        break

for i in range(13, len(message)):
    part = message[i-13:i+1]
    if isUnique(part):
        print(part, i+1)
        break