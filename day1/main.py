import heapq
from collections import Counter

from typing import Any


def pretty_print(part: int, result: Any):
    print("######################################")
    print(f"Part {part} answer:")
    print(result)
    print("######################################")

    return


def read_input():
    left, right = [], []

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            x = line.split()
            heapq.heappush(left, int(x[0]))
            heapq.heappush(right, int(x[1]))

    return left, right


def part_one():
    left, right = read_input()
    total = 0
    while len(left) and len(right):
        l, r = heapq.heappop(left), heapq.heappop(right)
        difference = abs(l - r)
        total += difference

    pretty_print(1, total)

    return total


def part_two():
    left, right = read_input()

    freq = Counter(right)

    similarity_score = sum([l * freq.get(l, 0) for l in left])

    pretty_print(2, similarity_score)

    return similarity_score


if __name__ == "__main__":
    part_one()
    part_two()
