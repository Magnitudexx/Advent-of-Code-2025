def parse_input(path: str):
    with open(path) as f:
        return f.read().strip().splitlines()


def specific_parse(data: list[str]):
    return [(n[0], int(n[1:])) for n in data]


class Dial:
    def __init__(self, start: int, maxi: int, data: list[tuple[str, int]]):
        self._state = start
        self._maxi = maxi + 1
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._data):
            rot, val = self._data[self._index]
            self._index += 1
            old_state = self._state
            passes = 0
            match rot:
                case "L":
                    self._state = (self._state - val) % self._maxi
                    while val > 0:
                        val -= 1
                        old_state -= 1
                        if old_state % self._maxi == 0:
                            passes += 1
                case "R":
                    self._state = (self._state + val) % self._maxi
                    while val > 0:
                        val -= 1
                        old_state += 1
                        if old_state % self._maxi == 0:
                            passes += 1
            return (self._state, passes)
        else:
            raise StopIteration


def part1(data):
    p_data: list[tuple[str, int]] = specific_parse(data)
    n: int = 0

    for state, _ in Dial(50, 99, p_data):
        if state == 0:
            n += 1
    return n


def part2(data):
    p_data: list[tuple[str, int]] = specific_parse(data)
    n: int = 0

    for state, rots in Dial(50, 99, p_data):
        n += rots
    print(n)
    return n


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
