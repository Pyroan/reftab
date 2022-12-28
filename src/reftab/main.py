import argparse
import datetime

import reftab.term as term
from .data import *


class reftab:
    name = "(this list)"
    ref_added = datetime.date(2022, 12, 27)
    ref_updated = datetime.date(2022, 12, 27)
    aliases = [
        "ls",
        "all",
        "reftab",
        "this"
    ]

    def __str__(self):
        tab = term.Table(title=" Available Tables ", columns=[
            term.Column(rows=[term.MAGENTA + x.aliases[0] +
                        term.RESET for x in tables]),
            term.Column(rows=[x.name for x in tables])
        ], sections=1)
        return str(tab)


tables = [
    # if this gets too big will switch to a quasi-observer pattern where tables register themselves in some
    # central data structure that main calls to instead
    reftab,
    asciitable,
    css_colors,
    ibm437,

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
        epilog="Supported Tables:\n"+", ".join(n.name for n in tables[1:]))
    parser.add_argument(
        "table", help="name of the desired reference table (IANA aliases also work)")
    args = parser.parse_args()
    t = fetch_table(args.table)
    if t == None:
        raise ValueError(f"Couldn't find table with name: {args.table}")
    else:
        try:
            print(t())
        except UnicodeEncodeError:
            raise ValueError(
                "The requested output doesn't support Unicode! Sorry!")
