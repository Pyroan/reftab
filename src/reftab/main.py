import argparse
from reftab.asciitable import asciitable

# def page437(): ...


tables = [
    # if this gets too big will switch to a quasi-observer pattern where tables register themselves in some
    # central data structure that main calls to instead
    asciitable
]


def fetch_table(name) -> object:
    """Return `table` from `tables` with `name` in `table.name` or `table.aliases`,
    or `None` if no such table was found.

    It should be guaranteed that the returned object has implemented a custom `__str__()` method which will
    format the table's data for display in the terminal"""

    for t in tables:
        if name.lower() in [t.name.lower()] + [*map(str.lower, t.aliases)]:
            return t
    return None


def run():
    parser = argparse.ArgumentParser(
        description="Fetch lil cheatsheets for data n such",
        epilog="Supported Tables:\n"+"\n".join(n.name for n in tables))
    parser.add_argument(
        "table", help="name of the desired reference table (IANA aliases also work)")
    args = parser.parse_args()
    t = fetch_table(args.table)
    if t == None:
        raise ValueError
    else:
        print(t())