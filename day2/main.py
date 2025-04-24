from typing import Any


def pretty_print(part: int, result: Any):
    print("######################################")
    print(f"Part {part} answer:")
    print(result)
    print("######################################")

    return


def is_report_safe(report: list[int]):
    increasing = report[1] > report[0]

    for i in range(1, len(report)):
        if increasing and report[i] <= report[i - 1]:
            return False
        if not increasing and report[i] >= report[i - 1]:
            return False

        if not (1 <= abs(report[i] - report[i - 1]) <= 3):
            return False

    return True


def part_one():
    """
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    """
    safe_reports = 0
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            report = [int(x) for x in line.split()]
            if is_report_safe(report):
                safe_reports += 1

    pretty_print(1, safe_reports)


if __name__ == "__main__":
    part_one()
