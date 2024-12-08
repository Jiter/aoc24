print(f"Advent of Code Day 3a")

import re

with open("input") as f:
    prg = f.read()

out = re.findall(r"don't\(\)|do\(\)|mul\(\d*,\d*\)", prg)

is_do = True
sol = 0


for line in out:
    
    if line == "don't()":
        is_do = False
    elif line == "do()":
        is_do = True
    elif is_do:
        tmp = re.search(r"\((\d*),(\d*)\)", line)
        sol = sol + (int(tmp[1]) * int(tmp[2]))        

print(f"Solution: {sol}")
