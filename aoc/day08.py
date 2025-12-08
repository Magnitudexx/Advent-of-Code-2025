import numpy as np


from numpy.typing import NDArray
from typing import LiteralString


def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()

def dist(node1, node2):
    return np.linalg.norm(np.array(node1) - np.array(node2))

def nearest_neighbor(junction:list[int], neighbors:list[list[int]]):
    local_neighbors = neighbors.copy()
    if junction in local_neighbors:
        local_neighbors.remove(junction)
    local_neighbors.sort(key=lambda x: dist(junction,x))

    return tuple(local_neighbors[0])

def part1(data: list[str]|list[LiteralString]):
    s_junctions:list[list[LiteralString]|list[str]] = [l.split(",") for l in data]
    junctions:list[list[int]] = [list(map(int, l)) for l in s_junctions] 

    a = {tuple(junction): nearest_neighbor(junction,junctions) for junction in junctions}
    superdict = dict(sorted(list(a.items()), key=lambda item: dist(list(item[0]),item[1])))
    circuits = []
    i = 0
    while i < 10:
        lst = list(superdict.items())
        key, value = lst[0]
        print(key,value)

        if (value, key) in lst:
            lst.remove((value, key))
        superdict = dict(lst)

        in_none = True
        for circuit in circuits:
            if key in circuit and value in circuit:
                in_none = False
            elif value in circuit:
                idx = circuit.index(value)
                if idx == 0:
                    circuit.insert(idx, key)
                else:
                    circuit += [key]
                junctions.remove(list(value))
                a = {tuple(junction): nearest_neighbor(junction,junctions) for junction in junctions}
                superdict = dict(sorted(list(a.items()), key=lambda item: dist(list(item[0]),item[1])))
                in_none = False
                i+=1
                
            

        if in_none:
            circuits.append([value, key])
            superdict.pop(key, None)
            i+=1

    print(circuits)
    length_list = list(map(len,circuits))
    length_list.sort(reverse=True)
    return np.prod(np.array(length_list[:3]))
def part2(data):
    pass


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
