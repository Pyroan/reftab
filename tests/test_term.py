import pytest
import reftab.term as t


def test_box_drawing_constants():
    # uses all of the 'light' box drawing characters (except for endcaps)
    standard_box = "┌─┬┐\n│ ││\n├─┼┤\n└─┴┘"
    my_box = f"{t.CORNER_UL}{t.LINE_HZ}{t.TSEP_D}{t.CORNER_UR}\n"\
        f"{t.LINE_VT} {t.LINE_VT}{t.LINE_VT}\n"\
        f"{t.TSEP_R}{t.LINE_HZ}{t.CROSS}{t.TSEP_L}\n"\
        f"{t.CORNER_DL}{t.LINE_HZ}{t.TSEP_U}{t.CORNER_DR}"
    assert my_box == standard_box

    # Now with double-lined...
    standard_box = "╔═╦╗\n║ ║║\n╠═╬╣\n╚═╩╝"
    my_box = f"{t.CORNER_UL_DOUBLE}{t.LINE_HZ_DOUBLE}{t.TSEP_D_DOUBLE}{t.CORNER_UR_DOUBLE}\n"\
        f"{t.LINE_VT_DOUBLE} {t.LINE_VT_DOUBLE}{t.LINE_VT_DOUBLE}\n"\
        f"{t.TSEP_R_DOUBLE}{t.LINE_HZ_DOUBLE}{t.CROSS_DOUBLE}{t.TSEP_L_DOUBLE}\n"\
        f"{t.CORNER_DL_DOUBLE}{t.LINE_HZ_DOUBLE}{t.TSEP_U_DOUBLE}{t.CORNER_DR_DOUBLE}"
    assert my_box == standard_box


@pytest.mark.skip
def test_box(): ...


class Test_Column():
    def test_width(self):
        # I know it's a little unintuitive for a value you manually set to 0 to get set to something else,
        # but the utility outweighs the awkwardness (and almost never comes up in practice)
        c = t.Column()
        assert c.width == 0
        c.rows = [
            "apple",
            "escargot",
            "banana",
        ]
        assert c.width == len('escargot')

        # introduce a cap...
        c.width = 3
        assert c.width == 3

        # remove the cap...
        c.width = 0
        assert c.width == len('escargot')

        # add a long title
        c.title = "Shopping List"
        assert c.width == len("Shopping List")

        # invalid setting
        with pytest.raises(ValueError):
            c.width = -1

    def test_alignment(self):
        c = t.Column()
        # default value
        assert c.alignment == "left"
        # invalid value
        with pytest.raises(ValueError):
            c.alignment = "centre"

        # outputs.
        c.rows = [
            "apple",
            "banana",
            "escargot"
        ]
        # "left" means spaces should be appended to the end (so later characters in the row get printed to the right place.)
        rows = str(c).splitlines()
        assert rows[0] == "apple   "
        assert rows[1] == "banana  "
        assert rows[2] == "escargot"

        c.alignment = "right"
        rows = str(c).splitlines()
        assert rows[0] == "   apple"
        assert rows[1] == "  banana"
        assert rows[2] == "escargot"

        #
        # `center`'s behavior can be different when the entry width & column width have different parities.
        # (i.e. when the number of leading/trailing spaces is odd)
        # we bias to the left in ambiguous cases.
        # (e.g. " corn  " as opposed to "  corn ")
        #
        c.alignment = "center"
        rows = str(c).splitlines()
        assert rows[0] == " apple  "
        assert rows[1] == " banana "
        assert rows[2] == "escargot"

    def test_title(self):
        c = t.Column(rows=["apple", "banana", "escargot"])
        assert len(str(c).splitlines()) == 3
        c.title = ("Shopping List")
        assert len(str(c).splitlines()) == 5

        with pytest.raises(ValueError):
            c.title = "I think I'm cool enough\n for Two Lines"


@pytest.mark.skip
def test_table(): ...
