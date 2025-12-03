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
    sp_data = data.split(",")
    ids = []
    for span in sp_data:
        le, he = tuple(span.split("-"))
        for num in range(int(le), int(he) + 1):
            s = str(num)
            l = len(s)
            idx1 = 0
            idx2 = 1
            width = 1
            pattern = s[0]
            while width <= l // 2:
                if s[idx1 : idx1 + width] == s[idx2 : idx2 + width]:
                    # idx2 = width
                    pattern = s[0:width]
                    width += 1
                elif (l // len(pattern)) * pattern == s:
                    print(num)
                    ids.append(num)
                else:
                    width += 1
                    idx2 = width
            if (l // len(pattern)) * pattern == s:
                print(num)
                ids.append(num)


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
