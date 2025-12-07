import numpy as np

from numpy.typing import NDArray


def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def part1(data: list[str]):
    start = data[0].index("S")
    data = data[1:]

    idxs = set([start])
    total = 0
    for line in data:
        np_line: NDArray[np.str_] = np.array(list(line))
        splitter_idxs = np.where(np_line == "^")[0]

        if splitter_idxs.size > 0:
            for idx in splitter_idxs:
                if idx in idxs:
                    idxs.remove(idx)
                    idxs.update([idx - 1, idx + 1])
                    total += 1

    return total


from collections import defaultdict


def part2(data):
    start = data[0].index("S")
    data = data[1:]

    idxs: dict[int, int] = defaultdict(int)
    idxs[start] = 1
    for line in data:
        np_line: NDArray[np.str_] = np.array(list(line))
        splitter_idxs = np.where(np_line == "^")[0]

        if splitter_idxs.size > 0:
            for idx in splitter_idxs:
                if idx in idxs:
                    idxs[idx - 1] += idxs[idx]
                    idxs[idx + 1] += idxs[idx]
            for idx in splitter_idxs:
                idxs[idx] = 0

    return sum(idxs.values())


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
