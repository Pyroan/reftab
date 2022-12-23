import argparse
from reftab.asciitable import asciitable

# def page437(): ...


names = {
    "ascii": asciitable,
    # "437": page437
}


def run():
    parser = argparse.ArgumentParser(
        description="Fetch lil cheatsheets for data n such",
        epilog="Supported Tables:\n"+"\n".join(n for n in names.keys()))
    parser.add_argument("table", help="the desired reference table")
    args = parser.parse_args()
    if args.table.lower() not in names:
        raise ValueError
    else:
        print(names[args.table.lower()]())
