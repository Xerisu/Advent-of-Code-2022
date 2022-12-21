from functools import cmp_to_key

with open("distress-signal.txt", "r") as input:
    signal = input.read()

signal2 = signal.split("\n")
signal = signal.split("\n\n")
signal = [s.split("\n") for s in signal]

for i in range(len(signal)):
    signal[i][0] = eval(signal[i][0])
    signal[i][1] = eval(signal[i][1])

# lewy ma być mniejszy lub równy od prawego, lewa lista ma być krótsza niż prawa
def checking_packets(left, right):
    if type(left) == int and type(right) == int:
        return left - right
    
    if type(left) == list and type(right) == list:
        for i in range(min(len(left), len(right))):
            if checking_packets(left[i], right[i]) != 0:
                return checking_packets(left[i], right[i])
        return len(left) - len(right)
           
    if type(left) == list and type(right) == int:
        
        return checking_packets(left, [right])
    
    if type(left) == int and type(right) == list:
        return checking_packets([left], right)
    
result = 0
for i in range(len(signal)):    
    if checking_packets(signal[i][0], signal[i][1]) <= 0:
        result += i + 1

print(result)

signal = [item for sublist in signal for item in sublist]
signal.append([[2]])
signal.append([[6]])
sorted_signal = sorted(signal, key=cmp_to_key(checking_packets))
result2 = 1
for i in range(len(sorted_signal)):
    if sorted_signal[i] == [[2]] or sorted_signal[i] == [[6]]:
        result2 *= i+1
print(result2)