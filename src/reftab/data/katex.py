import datetime
import reftab.term as t


class katex:
    """TeX functions supported by KaTeX (as of v0.16.4).
    Unfortunately it seems unlikely that terminals will be able to handle TeX output,
    I'll give UTF-8 approximates when possible, but hey,
    if you wanted something *thorough* you should probably check the real deal
    Source: https://katex.org/docs/supported.html"""
    name = "KaTeX Functions"
    ref_added = datetime.date(2022, 12, 26)
    ref_updated = datetime.date(2022, 12, 26)
    authority = "Khan Academy"
    source_introduced = "2014"  # original public release
    source_revised = "2022"  # latest major version released
    aliases = ["KaTeX", "TeX", "LaTeX", "math", "formulas", "equations"]
    data = {
        "KaTeX": []

        # "KaTeX > Accents": [
        #     ("a\u2032", [r"a'", r"a^{\prime}"]),
        #     ("a\u2033", [r"a''"]),
        #     ("\u00e1", [r"\acute{a}"]),
        #     ("\u0233", [r"\bar{y}"]),
        #     ("\u0103", [r"\breve{a}"]),
        #     ("\u01ce", [r"\check{a}"]),
        #     ("\u0227", [r"\dot{a}"]),
        #     ("\u00e4", [r"\ddot{a}"]),
        #     ("\u00e0", [r"\grave{a}"]),
        #     ("\u00e2", [r"\hat{a}"]),
        #     ("", [r"\widehat{ac}"]),
        #     ("\u00e3", [r"\tilde{a}"]),
        #     ("", [r"\widetilde{ac}"]),
        #     ("", [r"\utilde{AB}"]),
        #     ("", [r"\vec{F}"]),
        #     ("", [r"\overleftarrow{AB}"]),
        #     ("", [r"\underleftarrow{ab}"]),
        #     ("", [r"\overleftharpoon{ac}"]),
        #     ("", [r"\overleftrightarrow{AB}"]),
        #     ("", [r"\underleftrightarrow{AB}"]),
        #     ("", [r"\overline{AB}"]),
        #     ("", [r"\underline{AB}"]),
        #     ("", [r"\widecheck{ac}"]),
        #     ("\u00e5", [r"\mathring{a}"]),
        #     ("", [r"\overgroup{AB}"]),
        #     ("", [r"\undergroup{AB}"]),
        #     ("", [r"\Overrightarrow{AB}"]),
        #     ("", [r"\overrightarrow{AB}"]),
        #     ("", [r"\underrightarrow{AB}"]),
        #     ("", [r"\overrightharpoon{ac}"]),
        #     ("", [r"\overbrace{AB}"]),
        #     ("", [r"\underbrace{AB}"]),
        #     ("", [r"\overlinesegment{AB}"]),
        #     ("", [r"\underlinesegment{AB}"]),
        #     (f"{t.UNDERLINE}X{t.RESET}", [r"\underbar{X}"]),
        # ],
        # "KaTeX > Delimiters": [
        #     ("(", [r"(", r"\lparen"]),
        #     (")", [r")", r"\rparen"]),
        #     ("[", [r"[", r"\lbrack"]),
        #     ("]", [r"]", r"\rbrack"]),
        #     ("{", [r"\{", r"\lbrace"]),
        #     ("}", [r"\}", r"\rbrace"]),
        #     ("\u27e8", ["\u27e8", r"\langle", r"\lang"]),
        #     ("\u27e9", ["\u27e9", r"\rangle", r"\rang"]),
        #     ("\u2223", [r"|", r"\vert", r"\lvert", r"\rvert"]),
        #     ("\u2225", [r"\|", r"\Vert", r"\lVert", r"\rVert"]),
        #     ("<", [r"\lt"]),
        #     (">", [r"\gt"])
        # ]
    }

    def __str__(self):
        # title = f"{self.name} ({self.source_revised})"
        tables = []
        for name, entries in self.data.items():
            kcol = t.Column()
            vcol = t.Column()
            for k, v in entries:
                kcol.rows += [
                    f"{t.MAGENTA}{k}{t.RESET}" for _ in range(len(v))]
                vcol.rows += v
            tables.append(
                str(t.Table(title=name, columns=[kcol, vcol], sections=2)))
        return "".join(tables)


if __name__ == "__main__":
    print(katex())
