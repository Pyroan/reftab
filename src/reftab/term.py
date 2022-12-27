"""Helpers for nice terminal output
Uh oh this is swiftly becoming a god module for all string building/formatting. whoops."""
import math
import re
from typing import List

import colorama

colorama.just_fix_windows_console()

# color definitions
RESET = "\033[0m"
INVERTED = "\033[7m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
DIM = "\033[2m"

#
# Subset of UTF8 box drawing characters
# quick note on naming: the corners are named after where they "point" to, not
# after which of the 4 "cross" lines it uses (which is what unicode does)
# e.g. "CORNER_UL" (up-left) is  "┌", not "┘"
#
# T-Shaped "Separators" (TSEPs) are named after the direction their non-parallel line points.
# Yes this is the opposite of how corners work. It's inconsistent, but so is my brain.
# e.g. "TSEP_R" is "├", not "┤".
#
# oh and the directions are abbreviated as "U" for up, "D" for down, "L" for left, and
# "R" for right.
#
# arguably LINE_HZ could just as easily be called CORNER_LR but that would be silly
#
LINE_HZ = "\u2500"
LINE_VT = "\u2502"
CORNER_UL = "\u250c"
CORNER_UR = "\u2510"
CORNER_DL = "\u2514"
CORNER_DR = "\u2518"
TSEP_U = "\u2534"
TSEP_D = "\u252c"
TSEP_L = "\u2524"
TSEP_R = "\u251c"
CROSS = "\u253c"

CAP_U = "\u2575"
CAP_D = "\u2577"
CAP_L = "\u2574"
CAP_R = "\u2576"

#
# Words cannot describe how annoying the layout of this Unicode block is.
# There is simply no consistent pleasant way to get a specific character reference.
#
LINE_HZ_DOUBLE = "\u2550"
LINE_VT_DOUBLE = "\u2551"
CORNER_UL_DOUBLE = "\u2554"
CORNER_UR_DOUBLE = "\u2557"
CORNER_DL_DOUBLE = "\u255a"
CORNER_DR_DOUBLE = "\u255d"
TSEP_U_DOUBLE = "\u2569"
TSEP_D_DOUBLE = "\u2566"
TSEP_L_DOUBLE = "\u2563"
TSEP_R_DOUBLE = "\u2560"
CROSS_DOUBLE = "\u256c"


def rgb256(r: int, g: int, b: int) -> str:
    """Returns an escape code that will print text with the 8-bit color closest to the given 0..256 rgb values (at least on an xterm)"""
    # Hey turns out you can just, use fancy colors if you feel like it.
    # (fwiw my terminal seems to support TrueColor but hey, X11 colors should still be correct when cast to 8bit)
    # map each component from 0..256 to 0..6
    r, g, b = map(lambda x: int(x/255*5+0.5), [r, g, b])
    # Offset by 16 because 0x0..0xF are used for base colors

    return f"\033[38;5;{r*36 + g*6 + b + 16}m"


def rgb24bit(r: int, g: int, b: int) -> str:
    # Like above, but for terminals that support TrueColor and don't need to throw away accuracy
    return f"\033[38;2;{r};{g};{b}m"


def esc_len(s):
    """Escaped Length: len() but excluding non-visible ansi escape codes."""
    return len(re.sub(chr(27)+r"\[.+?m", "", s))


def align(s: str, alignment: str, width: int):
    # s = s.strip() # turns out this was breaking more than it was protecting.
    offset = " " * (width - esc_len(s))
    if alignment == "left":
        s += offset
    elif alignment == "right":
        s = offset + s
    elif alignment == "center":
        pivot = len(offset)//2 + (len(offset) % 2)
        s = offset[pivot:] + s + offset[:pivot]
    else:
        raise ValueError("Invalid alignment")
    return s


def box(body: str, header: str = None) -> str:
    """Return a string that draws `body` and `header` inside a box using UTF-8 Box Drawing characters"""
    body = body.splitlines()
    if header:
        header = header.strip()
    else:
        header = ""
    width = max([esc_len(x) for x in body+[header]])
    s = f"{CORNER_UL_DOUBLE}{width*LINE_HZ_DOUBLE}{CORNER_UR_DOUBLE}\n"
    if header != "":
        s += f"{LINE_VT_DOUBLE}{align(header,'center',width)}{LINE_VT_DOUBLE}\n"
        s += f"{TSEP_R_DOUBLE}{width*LINE_HZ_DOUBLE}{TSEP_L_DOUBLE}\n"
    for line in body:
        s += f"{LINE_VT_DOUBLE}{align(line,'left',width)}{LINE_VT_DOUBLE}\n"
    s += f"{CORNER_DL_DOUBLE}{width*LINE_HZ_DOUBLE}{CORNER_DR_DOUBLE}\n"
    return s


class Column:
    """A column for holding arbitrary data in a Table
    (we don't need to organize this by records like a database, since for now we're always printing tables all at once,
    so for formatting it's more pragmatic to organize this by "fields")

    Default values for keyword args:

    `title`: optional, if no other rows in the table have titles either, only the rows will be printed.
    `rows`: (ordered) List of data entires to displayed in the column
    `width`: in terminal columns (characters). if 0, will be automatically set to fit the longest entry; if >0, will trim any entries too long to fit.
    `alignment`: one of `"left"`, `"right"`, `"center"`; sets alignment for header and all entries. `"left"` by default.
    """

    def __init__(self, title: str = "", rows: list = None, width: int = 0, align: str = "left"):
        if rows == None:
            rows = []
        self.title = title
        self.rows = rows

        self.width = width
        self.height = len(self.rows) + 1 + (1 if self.title else 0)

        self.alignment = align

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        if "\n" in value:
            raise ValueError("Column titles cannot contain newlines")
        self._title = value

    @property
    def width(self) -> int:
        # This feels like a HACK but we're going to set _width inside the getter. Lol.
        return max(esc_len(x) for x in self.rows+[self.title]) if self._auto_width else self._width

    @width.setter
    def width(self, value: int):
        if value < 0:
            raise ValueError("Column width can't be negative")
        elif value == 0:
            self._auto_width = True
        else:
            self._auto_width = False
            self._width = value

    @property
    def alignment(self):
        return self._alignment

    @alignment.setter
    def alignment(self, value):
        if value not in ["left", "right", "center"]:
            raise ValueError(f"Invalid alignment: {repr(value)}")
        self._alignment = value

    def __str__(self):
        if len(self.rows) == 0:
            # debating whether printing an empty Column should raise a ValueError or just happen...
            return ""
        s = ""
        if self.title:
            s += align(self.title, self.alignment, self.width) + "\n"
            s += LINE_HZ * self.width + "\n"
        for r in self.rows:
            s += align(r, self.alignment, self.width) + "\n"
        return s


class Table:
    """A structure that stores/displays multiple Columns of data.

    `sections` is the number of roughly equal parts the table will be split into when it is displayed
    (to save space). If greater than the number of columns, empty sections will be ignored (not printed)
    """

    def __init__(self, title: str = "", columns: List[Column] = None, sections=1):
        if columns == None:
            columns = []
        self.title = title  # i'll do validations later or not.
        self.columns = columns
        self.sections = sections

    @property
    def sections(self):
        return self._sections

    @sections.setter
    def sections(self, value):
        if type(value) != int or value < 1:
            raise ValueError("Invalid number of sections (must be an int >=1")
        self._sections = value

    def __str__(self):
        # This function will be published in my obituary as one of my worst sins.
        if len(self.columns) == 0:
            return ""
        body = ""
        cols = [str(c).splitlines() for c in self.columns]

        sections = min(self.sections, max(len(c.rows) for c in self.columns))
        # Titles, if there's any.
        if not all(c.title == "" for c in self.columns):
            headers = f" {BOLD}"+f" {RESET}{LINE_VT}{BOLD} ".join([f" ".join(c[0]
                                                                             for c in cols)]*sections) + f"{RESET} \n"
            headers += CAP_R + \
                f"{LINE_HZ}{CROSS}{LINE_HZ}".join([f"{LINE_HZ}".join(c[1]
                                                                     for c in cols)]*sections) + CAP_L + "\n"
            body += headers
            cols = [c[2:] for c in cols]

        # rows ("Entries")
        entry_index = 0
        height = math.ceil(
            max(len(c) for c in cols)/sections)
        while entry_index < height:
            row = []
            for e in range(entry_index, max(len(c)for c in cols), height):
                row += [" "+" ".join(c[e] for c in cols)+" "]
            entry_index += 1
            row += [""] * (sections-len(row))
            body += LINE_VT.join(row) + "\n"

        return box(body, f"{BOLD}{self.title}{RESET}")
