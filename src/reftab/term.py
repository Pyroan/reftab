import re

import colorama

colorama.just_fix_windows_console()


reset = "\033[0m"
bold = "\033[1m"
underline = "\033[4m"
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
dim = "\033[2m"


def esc_len(s):
    return len(re.sub(chr(27)+r"\[\d+m", "", s))


def box(body: str, header: str = None) -> str:
    """just a test to draw boxes dwai"""
    b = body.splitlines()
    m = max([esc_len(x) for x in b+[header]])
    s = ""
    s += "\u2554"+m*"\u2550"+"\u2557\n"
    if header != None:
        offset = (m-esc_len(header)-2) // 2
        s += "\u2551 "+" "*offset + header + " "*offset + " \u2551\n"
        s += "\u255f"+m*"\u2500"+"\u2562\n"
    for i in b:
        s += "\u2551" + i + " "*(m-esc_len(i)-2) + "\u2551\n"
    s += "\u255a"+m*"\u2550"+"\u255d\n"
    return s
