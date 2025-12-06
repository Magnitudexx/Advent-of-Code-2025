import re
import numpy as np

from aoc.utils import get_neighbors
from numpy.typing import NDArray


def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def part1(data):
    ops = re.findall(r"[+*]",data[-1])
    data = data[:-1]
    num_list = [re.findall(r"[0-9]+", l) for l in data]
    arr: NDArray[np.str_] = np.array(num_list, dtype=str)
    i_arr = arr.astype(int)
    rows, cols = arr.shape
    total = 0
    for i, op in enumerate(ops):
        col = i_arr[:,i]

        match op:
            case "+":
                total += col.sum()
            case "*":
                total += col.prod()

    return total

def part2(data):
    ops = re.findall(r"[+*][ ]+",data[-1])
    data = data[:-1]
    num_list = [list(l) for l in data]
    arr: NDArray[np.str_] = np.array(num_list, dtype=str)
    rows, cols = arr.shape
    total = 0
    idx:int = 0
    for op in ops:
        sub_arr = arr[:,idx:idx +len(op)]
        l_sub = len(sub_arr)
        nums = []
        for i in range(len(op)):
            s = "".join(list(sub_arr[:,i])).strip()
            if s != '':
                nums.append(int(s))

        nums = np.array(nums)
        match op.strip():
            case "+":
                total += nums.sum()
            case "*":
                total += nums.prod()
        idx += len(op)

    return total


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
