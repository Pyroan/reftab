"""Helpers for nice terminal output"""
import re

import colorama

colorama.just_fix_windows_console()

# color definitions
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
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


def esc_len(s):
    return len(re.sub(chr(27)+r"\[\d+m", "", s))


def box(body: str, header: str = None) -> str:
    """Return a string that draws `body` and `header` inside a box using UTF-8 Box Drawing characters"""
    b = body.splitlines()
    m = max([esc_len(x) for x in b+[header]])
    s = f"{CORNER_UL_DOUBLE}{m*LINE_HZ_DOUBLE}{CORNER_UR_DOUBLE}\n"
    if header != None:
        offset = (m-esc_len(header)-2) // 2
        s += f"{LINE_VT_DOUBLE} {' '*offset}{header}{' '*offset} {LINE_VT_DOUBLE}\n"
        s += f"{TSEP_R_DOUBLE}{m*LINE_HZ_DOUBLE}{TSEP_L_DOUBLE}\n"
    for i in b:
        s += f"{LINE_VT_DOUBLE}{i}{' '*(m-esc_len(i)-2)}{LINE_VT_DOUBLE}\n"
    s += f"{CORNER_DL_DOUBLE}{m*LINE_HZ_DOUBLE}{CORNER_DR_DOUBLE}\n"
    return s
