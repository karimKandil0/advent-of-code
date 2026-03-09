import sys
import re

def part1(data):
    memory = "".join(data)

    matches = re.findall(r"mul\((\d+),(\d+)\)", memory)

    total = 0
    for a, b in matches:
        total += int(a) * int(b)

    return total

def part2(data):
    pass

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
