import sys
from collections import Counter

def parse(data):
    left = []
    right = []

    for line in data: 
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)

    return left, right

def part1(data):

    left, right = parse(data)

    left.sort()
    right.sort()

    total = 0
    for a, b in zip(left, right):
        total += abs(a - b)

    return total

def part2(data):
    left, right = parse(data)

    counts = Counter(right)

    score = 0
    for x in left:
        score += x * counts[x]

    return score

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
