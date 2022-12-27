import datetime
import reftab.term as t


class ibm437:
    name = "IBM437"
    ref_added = datetime.date(2022, 12, 26)
    ref_updated = datetime.date(2022, 12, 26)
    authority = "IBM"
    source_introduced = "1981"  # year IBM PC was released

    # https://www.iana.org/assignments/character-sets/character-sets.xhtml
    source_revised = "1990"
    aliases = ["cp437", "437", "csPC8CodePage437",
               "OEM-US"]
    notes = ("The mapping from CP437 to Unicode equivalents isn't 1:1, and there's been a lot of debate on how to translate the encodings over the years. "
             "However, these details are out of Reftab's scope so we're ignoring a lot of the nuance here. "
             "Characters are colored RED when they're equivalent to ASCII's character at that codepoint, and BLUE otherwise"
             )
    data = [
        r"\0", "\u263a", "\u263b", "\u2665", "\u2666", "\u2663", "\u2660", "\u2022", "\u25d8", "\u25cb", "\u25d9", "\u2642", "\u2640", "\u266a", "\u266b", "\u263c",
        "\u25ba", "\u25c4", "\u2195", "\u203c", "\u00b6", "\u00a7", "\u25ac", "\u21a8", "\u2191", "\u2193", "\u2192", "\u2190", "\u221f", "\u2194", "\u25b2", "\u25bc",
        *[chr(i) for i in range(0x20, 0x7f)], "\u2302",
        # Spot the point where I said "this is silly"
        *[chr(c)for c in (0xc7, 0xfc, 0xe9, 0xe2, 0xe4, 0xe0, 0xe5, 0xe7, 0xea, 0xeb, 0xe8, 0xef, 0xee, 0xec, 0xc4, 0xc5,
                          0xc9, 0xe6, 0xc6, 0xf4, 0xf6, 0xf2, 0xfb, 0xf9, 0xff, 0xd6, 0xdc, 0xa2, 0xa3, 0xa5, 0x20a7, 0x192,
                          0xe1, 0xed, 0xf3, 0xfa, 0xf1, 0xd1, 0xaa, 0xba, 0xbf, 0x2310, 0xac, 0xbd, 0xbc, 0xa1, 0xab, 0xbb,
                          0x2591, 0x2592, 0x2593, 0x2502, 0x2524, 0x2561, 0x2562, 0x2556, 0x2555, 0x2563, 0x2551, 0x2557, 0x255d, 0x255c, 0x255b, 0x2510,
                          0x2514, 0x2534, 0x252c, 0x251c, 0x2500, 0x253c, 0x255e, 0x255f, 0x255a, 0x2554, 0x2569, 0x2566, 0x2560, 0x2550, 0x256c, 0x2567,
                          0x2568, 0x2564, 0x2565, 0x2559, 0x2558, 0x2552, 0x2553, 0x256b, 0x256a, 0x2518, 0x250c, 0x2588, 0x2584, 0x258c, 0x2590, 0x2580,
                          0x3b1, 0x0df, 0x393, 0x3c0, 0x3a3, 0x3c3, 0xb5, 0x3c4, 0x3a6, 0x398, 0x3a9, 0x3b4, 0x221e, 0x3c6, 0x3b5, 0x2229,
                          0x2261, 0xb1, 0x2265, 0x2264, 0x2320, 0x2321, 0xf7, 0x2248, 0xb0, 0x2219, 0xb7, 0x221a, 0x207f, 0xb2, 0x25a0)],
        "NBSP"
    ]

    def __str__(self):
        title = f"{self.name} ({self.source_revised})"
        dec = t.Column("Dec", align="right")
        hx = t.Column("Hx", align="right")
        ch = t.Column("Chr")
        for i, c in enumerate(self.data):
            dec.rows += [str(i)]
            hx.rows += [f"{i:X}"]
            ch.rows += [
                f"{t.MAGENTA if i in [*range(1,0x20),*range(0x7f,0x100)]else t.RED}{c}{t.RESET}"]

        tab = t.Table(title=title, columns=[dec, hx, ch], sections=4)
        return str(tab)


if __name__ == "__main__":
    print(ibm437())
