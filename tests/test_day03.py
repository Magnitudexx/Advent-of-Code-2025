from aoc.day03 import part1, part2, parse_input


sample = """987654321111111
811111111111119
234234234234278
818181911112111"""

data = sample.strip().splitlines()


def test1():
    assert part1(data) == 357


def test2():
    assert part2(data) == 3121910778619
