import heapq


def main():
    left, right = [], []

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            x = line.split()
            heapq.heappush(left, int(x[0]))
            heapq.heappush(right, int(x[1]))

    total = 0
    while len(left) and len(right):
        l, r = heapq.heappop(left), heapq.heappop(right)
        difference = abs(l - r)
        total += difference

    print(total)

    return total


if __name__ == "__main__":
    main()
