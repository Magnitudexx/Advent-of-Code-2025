import re
import numpy as np

from aoc.utils import get_neighbors
from numpy.typing import NDArray


def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().strip().splitlines()


def part1(data):
    lst: list[list[str]] = [list(s) for s in data]
    arr: NDArray[np.str_] = np.array(lst, dtype=str)
    col, row = arr.shape
    count = 0
    for i in range(col):
        for j in range(row):
            if arr[i, j] == "@":
                neighbors = get_neighbors(arr, i, j)
                condition = neighbors == "@"
                if np.extract(condition, neighbors).size < 4:
                    count += 1
    return count


def part2(data):
    lst: list[list[str]] = [list(s) for s in data]
    arr: NDArray[np.str_] = np.array(lst, dtype=str)
    col, row = arr.shape
    full_count = 0
    while True:
        count = 0
        for i in range(col):
            for j in range(row):
                if arr[i, j] == "@":
                    neighbors = get_neighbors(arr, i, j)
                    condition = neighbors == "@"
                    if np.extract(condition, neighbors).size < 4:
                        count += 1
                        arr[i, j] = "x"
        if count == 0:
            break
        full_count += count
    return full_count


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
