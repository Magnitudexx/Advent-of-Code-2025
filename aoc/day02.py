import re


def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read()


def part1(data):
    sp_data = data.split(",")
    ids = []
    for span in sp_data:
        le, he = tuple(span.split("-"))
        for num in range(int(le), int(he) + 1):
            s = str(num)
            l = len(s)
            if l % 2 == 0:
                if s[0 : (l // 2)] == s[l // 2 :]:
                    print(num)
                    ids.append(num)

    return sum(ids)


def part2(data):
    pass


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
