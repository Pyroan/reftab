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


def test_box(): ...
