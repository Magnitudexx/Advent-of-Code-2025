def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def part1(data: list[str]):
    idx = data.index("")
    ranges: list[tuple[int, int]] = []
    for r in data[:idx]:
        low, high = r.split("-")
        ranges.append((int(low), int(high)))

    ids: list[int] = [int(i) for i in data[idx + 1 :]]
    count = 0
    for i in ids:
        for low, high in ranges:
            if i >= low and i <= high:
                count += 1
                break
    return count


def part2(data):
    idx = data.index("")
    ranges: list[tuple[int, int]] = []
    for r in data[:idx]:
        low, high = r.split("-")
        ranges.append((int(low), int(high)))
    ranges.sort(reverse=True, key=lambda x: x[1])
    p_ranges: list[tuple[int, int]] = []
    count = 0
    overlap = False
    for low, high in ranges:
        for p_low, p_high in p_ranges:
            # check if totally within a range
            if low >= p_low and high <= p_high:
                count -= high - low + 1
                break
            # otherwise we may need to trim lower bound and higher bound
            if low < p_low and high >= p_low:
                high = p_low - 1

            if low <= p_high and high >= p_high:
                low = p_high + 1

        # when range is legal we add it to count
        count += high - low + 1
        p_ranges.append((low, high))
    return count


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
