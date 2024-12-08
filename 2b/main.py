print(f"Advent of Code Day 2")

def calc(report):
        desc = False
        if report[0] > report[1]:
            desc = True

        safe = True
        
        for num in range(0, len(report)-1):
            if abs(report[num] - report[num + 1]) > 3:
                safe = False
                print("1")
                break

            if not desc and report[num] >= report[num + 1]:
                safe = False
                print("2")
                break
            
            if desc and report[num] <= report[num + 1]:
                safe = False
                print("3")
                break

        if safe:
            return 1
        return 0


with open("input") as f:
    data = f.read().splitlines()

a = list()
b = list()

z = 0

for line in data:
    report = list(map(int,line.split(" ")))

    print(f"\nreport: {report}")

    if calc(report) == 0:
        for i in range(0, len(report)):
            new_list = report.copy()

            del new_list[i]

            if calc(new_list) == 1:
                z += 1
                break
    else:
        z += 1

print(z)





        


print(f"The Value is {z}")


def shit():
            if all(1 <= abs(num) <= 3 for num in slope):
                z = z + 1
                #continue
            else:
                print('selse')
                print(slope)
            if any(0 == num for num in slope):
                slope.remove(0)
            else:
                print(f"report: {report}")
                print(f"slope: {slope}")

                idx = slope.index(max(slope, key=abs))
                if idx != 0:
                    del report[idx+1]

                print(f"report2: {report}")
                slope = calc_slope(report)
                            
            if all(1 <= abs(num) <= 3 for num in slope):
                z = z + 1
                print(f"found one >= {z}")
                print(report)
                
                    