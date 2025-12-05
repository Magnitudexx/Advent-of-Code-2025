

def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def part1(data:list[str]):
    idx = data.index('')
    ranges:list[tuple[int,int]] = []
    for r in data[:idx]:
        low, high = r.split('-')
        ranges.append((int(low), int(high)))

    ids:list[int] = [int(i) for i in data[idx+1:]]
    count = 0
    for i in ids:
        for low, high in ranges:
            if i >= low and i <= high:
                count += 1
                break
    return count
def part2(data):
    pass

if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
