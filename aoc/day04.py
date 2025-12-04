import re
import numpy as np
from numpy.typing import NDArray


def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().strip().splitlines()

def get_neighbors(arr, r, c, include_self=False):
    # Determine slice bounds, staying inside array limits
    r_min = max(0, r - 1)
    r_max = min(arr.shape[0], r + 2)
    c_min = max(0, c - 1)
    c_max = min(arr.shape[1], c + 2)

    # Extract the region
    region = arr[r_min:r_max, c_min:c_max]

    if include_self:
        return region
    else:
        # Remove center element
        neighbors = region.copy().reshape(-1)
        neighbors = np.delete(neighbors, (r - r_min) * region.shape[1] + (c - c_min))
        return neighbors

def part1(data):
    lst:list[list[str]] = [list(s) for s in data]
    arr:NDArray = np.array(lst, dtype=str)
    col, row = arr.shape
    count = 0
    for i in range(col):
        for j in range(row):
            if arr[i,j] == '@':
                neighbors = get_neighbors(arr,i,j)
                condition = neighbors == '@'
                if np.extract(condition,neighbors).size < 4:
                    count += 1
    return count

 
def part2(data):
    pass


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
