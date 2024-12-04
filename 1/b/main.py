print(f"Advent of Code Day 1 Part 2")

with open("input") as f:
    data = f.read().splitlines()

a = list()
b = list()

for line in data:
    tmp = line.split("   ")
    a.append(int(tmp[0]))
    b.append(int(tmp[1]))


sum = 0

for val in a:
    z = b.count(val)
    sum = sum + (val*z)

print(f"The Value is {sum}")
