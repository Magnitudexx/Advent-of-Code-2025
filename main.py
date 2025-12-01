
# ▶️ main.py (Runner CLI)
import importlib
from rich import print

def run_day(day: int):
    mod = importlib.import_module(f"aoc.day{day:02}")
    data = mod.parse_input(f"inputs/day{day:02}.txt")
    print(f"[bold green]Day {day:02}[/bold green]")
    print("[cyan]Part 1:[/cyan]", mod.part1(data))
    print("[cyan]Part 2:[/cyan]", mod.part2(data))

def cli():
    import sys
    if len(sys.argv) < 2:
        print("[red]Usage:[/red] aoc <day>")
        return
    run_day(int(sys.argv[1]))

if __name__ == "__main__":
    cli()

