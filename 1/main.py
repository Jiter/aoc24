f_data = open("input", "r")

data = f_data.read()

data_into_list= data.split("\n")

a = list()
b = list()

for line in data_into_list:
    tmp = line.split("   ")
    a.append(int(tmp[0]))
    b.append(int(tmp[1]))

a.sort()
b.sort()

z = 0

for i, j in zip(a,b):
    z = z + abs(i-j)

print(f"The Value is {z}")
