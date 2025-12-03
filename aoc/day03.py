import re


def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().strip().splitlines()


def part1(data):
    b = []
    for bank in data:
        first: int = 0
        sec: int = 0
        last = len(bank) - 1
        for i, num in enumerate(bank):
            if first == 9 and sec == 9:
                break
            elif int(num) > first and i != last:
                first = int(num)
                sec = 0
            elif int(num) > sec:
                sec = int(num)

        b.append(10 * first + sec)
    return sum(b)


def part2(data):
    b = []
    for bank in data:
        num_arr: list[str] = ["0" for _ in range(12)]
        last = len(bank) - 1
        for i, num in enumerate(bank):
            for n in range(12):
                if int(num) > int(num_arr[n]) and last - i >= 12 - n - 1:
                    num_arr[n] = num
                    num_arr[n + 1 :] = ["0" for _ in range(len(num_arr[n + 1 :]))]
                    break
                elif i == last:
                    if int(num) > int(num_arr[-1]):
                        num_arr[-1] = num

        s = "".join(num_arr)
        b.append(int(s))
    return sum(b)


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
