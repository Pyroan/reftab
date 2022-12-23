import datetime

import reftab.term as t


class asciitable:
    """I keep acting like my plan wasn't to hard code these from the beginning.
    Everything else has been my overengineering instincts trying to trick me
    into making a useful database instead of my personal crib sheets."""
    name = "US-ASCII"
    # metadata
    ref_added = datetime.date(2022, 12, 22)
    ref_updated = datetime.date(2022, 12, 22)
    authority = "IANA"
    source_introduced = "1963"
    source_revised = "1986"
    aliases: list[str] = [
        "iso-ir-6",
        "ANSI_X3.4-1968",
        "ANSI_X3.4-1986",
        "ISO_646.irv:1991",
        "ISO646-US",
        "ASCII",
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
        title = f"{t.bold}{self.name} ({self.source_revised}){t.reset}"
        body = "\u2502".join([f" {t.bold}Dec Hx Chr{t.reset} "]*4)+"\n"
        body += "\u253c".join(["\u2500"*12]*4)+"\n"
        for i in range(32):
            for j in range(4):
                body += f"{t.white}{i+(32*j):>4} {i+(32*j):>2X}{t.reset} {t.red}{self.data[i+(32*j)]:<3}{t.reset} "
                if j < 3:
                    body += "\u2502"
            body += "\n"
        return t.box(body, title)


if __name__ == "__main__":
    print(asciitable())
