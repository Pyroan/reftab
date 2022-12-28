import datetime
from typing import List

import reftab.term as t


class asciitable:
    """I keep acting like my plan wasn't to hard code these from the beginning.
    Everything else has been my overengineering instincts trying to trick me
    into making a useful database instead of my personal crib sheets."""
    name = "US-ASCII"
    # metadata
    ref_added = datetime.date(2022, 12, 22)
    ref_updated = datetime.date(2022, 12, 27)
    authority = "ANSI"
    source = "https://www.iana.org/assignments/character-sets/character-sets.xhtml"
    source_introduced = "1963"
    source_revised = "1986"
    aliases = [
        "ascii",
        "iso-ir-6",
        "ANSI_X3.4-1968",
        "ANSI_X3.4-1986",
        "ISO_646.irv:1991",
        "ISO646-US",
        "us",
        "IBM367",
        "cp367",
        "csASCII"
    ]
    data = [
        r"\0", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", r"\a", r"\b", r"\t", r"\n", r"\v", r"\f", r"\r", "SO", "SI",
        "DLE", "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN", "EM", "SUB", r"\e", "FS", "GS", "RS", "US"
    ] + [chr(x) for x in range(32, 127)] + ["DEL"]

    def __str__(self):
        title = f"{self.name} ({self.source_revised})"
        tab = t.Table(title=title, columns=[
            t.Column("Dec", [f"{i}"for i in range(128)], align="right"),
            t.Column("Hx", [f"{i:X}"for i in range(128)], align="right"),
            t.Column("Chr", [f"{t.RED}{c}{t.RESET}" for c in self.data])
        ], sections=4)
        return str(tab)


if __name__ == "__main__":
    print(asciitable())
