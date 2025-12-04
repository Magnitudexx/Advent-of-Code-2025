from aoc.day04 import part1, part2, parse_input


sample = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

data = sample.strip().splitlines()


def test1():
    assert part1(data) == 13


def test2():
    assert part2(data) == 43
