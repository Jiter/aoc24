print(f"Advent of Code Day 3a")

import re

with open("input") as f:
    prg = f.read()

out = re.findall(r"mul\((\d*),(\d*)\)", prg)

sol = 0

for match in out:
    tmp = int(match[0]) * int(match[1])
    sol = sol + tmp

print(f"Solution: {sol}")
