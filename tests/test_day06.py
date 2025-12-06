from aoc.day06 import part1, part2


sample ="""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """ 
data = sample.splitlines()


def test1():
    assert part1(data) == 4277556


def test2():
    assert part2(data) == 3263827
