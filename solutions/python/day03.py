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
    memory = "".join(data)
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    instructions = re.finditer(pattern, memory)

    total = 0
    enabled = True

    for match in instructions:
        text = match.group()

        if text == "do()":
            enabled = True

        elif text == "don't()":
            enabled = False

        else:
            a, b = match.groups()
            if enabled:
                total += int(a) * int(b)

    return total

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
