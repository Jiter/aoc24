print(f"Advent of Code Day 2")

with open("input") as f:
    data = f.read().splitlines()

a = list()
b = list()
save = 0
z = 0

for line in data:
    report = list(map(int,line.split(" ")))
    rev = sorted(report)
    rev.reverse()
    if report == sorted(report) or report == rev:
        print (report)

        good = True
        first = True
        for val in report:   
            if first: 
                save = val
                first = False
                continue

            if not (abs(val - save)) in range (1,4) and save != 0:
                good = False
                save = 0
                break

            save = val

        if good == True:
            z = z + 1

print(f"The Value is {z}")
