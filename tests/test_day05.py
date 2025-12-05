from aoc.day05 import part1, part2, parse_input


sample = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
data = sample.splitlines()


def test1():
    assert part1(data) == 3


def test2():
    assert part2(data) == 14
