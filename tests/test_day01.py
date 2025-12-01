from aoc.day01 import part1, part2

def test_examples():
    sample = ["L68",
"L30",
"R48",
"L5",
"R60",
"L55",
"L1",
"L99",
"R14",
"L82"]
    assert part1(sample) == 3
    assert part2(sample) == 6

def test2():
    sample = ["L101","R101"]
    assert part2(sample) == 2


