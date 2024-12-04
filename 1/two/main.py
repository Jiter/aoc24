print(f"Advent of Code Day 2")

f_data = open("input", "r")

data = f_data.read()

data_into_list= data.split("\n")

a = list()
b = list()

for line in data_into_list:
    tmp = line.split("   ")
    a.append(int(tmp[0]))
    b.append(int(tmp[1]))

sum = 0

for val in a:
    z = b.count(val)
    sum = sum + (val*z)

print(f"The Value is {sum}")
