import re
import numpy as np

from aoc.utils import get_neighbors
from numpy.typing import NDArray


def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def part1(data:list[str]):
    start = data[0].index('S')
    data = data[1:]

    idxs = set([start])
    total = 0
    for line in data:
        np_line:NDArray[np.str_] = np.array(list(line))
        splitter_idxs = np.where(np_line == '^')[0]

        tmp_idxs:set[int] = set([])
        if splitter_idxs.size > 0:
            for idx in splitter_idxs:
                if idx in idxs:
                    idxs.remove(idx)
                    idxs.update([idx-1, idx+1])
                    total += 1

    return total

import heapq
def part2(data):
    start_col = data[0].index('S')
    arr = np.array([list(line) for line in data])
    start = (0, start_col)

    q:list[tuple[int,int]] = [start]
    heapq.heapify(q)
    total = 0
    terminated = True
    rows, cols = arr.shape
    while len(q) > 0:
        row, col = heapq.heappop(q)
        c:NDArray = arr[row+1:,col]
        if '^' in c:
            idx = list(c.flatten()).index('^')
            heapq.heappush(q,(row+idx,col-1))
            heapq.heappush(q,(row+idx,col+1))
        else:
            total += 1
    return total


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
