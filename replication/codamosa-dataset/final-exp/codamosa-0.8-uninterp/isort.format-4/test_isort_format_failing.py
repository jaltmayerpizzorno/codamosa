# Automatically generated by Pynguin.
import isort.format as module_0
import pathlib as module_1
import typing as module_2

def test_case_0():
    try:
        str_0 = 'F\rd8'
        bool_0 = module_0.ask_whether_to_apply_changes_to_file(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Sorts the literal present within the provided code against the provided sort type,\n    returning the sorted representation of the source code.\n    '
        str_1 = module_0.format_natural(str_0)
        str_2 = '#)Y_2d!Ni3@$7lN^g'
        str_3 = module_0.format_simplified(str_2)
        colorama_printer_0 = module_0.ColoramaPrinter()
        optional_0 = None
        colorama_printer_1 = module_0.ColoramaPrinter(optional_0)
        str_4 = 'b>hs_)"~`i:'
        colorama_printer_1.diff_line(str_4)
        str_5 = module_0.format_simplified(str_1)
        bytes_0 = b'\xd9\xeb\xf08\xe1\x88\\\xae\x9e~\xeb[\xda'
        path_0 = module_1.Path()
        var_0 = path_0.open(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = None
        str_0 = 'Sorts the literal present within the provided code against the provided sort type,\n    returning the sorted representation of the source code.\n    '
        str_1 = module_0.format_natural(str_0)
        str_2 = module_0.format_simplified(str_0)
        str_3 = module_0.format_natural(str_1)
        str_4 = 'F{g'
        str_5 = 'Y:Fm'
        str_6 = module_0.remove_whitespace(str_5)
        str_7 = 'C=KE^L.6zr.v.=sd~5\r'
        colorama_printer_0 = module_0.ColoramaPrinter()
        colorama_printer_0.diff_line(str_4)
        bool_1 = True
        basic_printer_0 = module_0.BasicPrinter()
        var_0 = module_0.create_terminal_printer(bool_1)
        path_0 = None
        text_i_o_0 = module_2.TextIO()
        text_i_o_1 = text_i_o_0.__enter__()
        var_1 = module_0.show_unified_diff(file_input=str_7, file_output=str_0, file_path=path_0, output=text_i_o_1, color_output=bool_0)
        str_8 = 'Q22cw|'
        colorama_printer_0.diff_line(str_4)
        bool_2 = module_0.ask_whether_to_apply_changes_to_file(str_8)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Sorts the iteral present within the provided code against the provided sort type,\n    returning the sorted representation of the source code\n    '
        str_1 = module_0.format_natural(str_0)
        str_2 = module_0.format_simplified(str_1)
        str_3 = ",*|Lrg>vA '&e"
        str_4 = module_0.remove_whitespace(str_3)
        colorama_printer_0 = module_0.ColoramaPrinter()
        str_5 = 'D>G$1(~W,'
        colorama_printer_0.diff_line(str_5)
        basic_printer_0 = module_0.BasicPrinter()
        bool_0 = True
        var_0 = module_0.create_terminal_printer(bool_0)
        text_i_o_0 = module_2.TextIO()
        list_0 = [bool_0]
        text_i_o_1 = module_2.TextIO(*list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\x0cP)%D#jG3Tp`(amJ'
        str_1 = module_0.format_natural(str_0)
        str_2 = module_0.format_simplified(str_0)
        str_3 = module_0.format_natural(str_1)
        str_4 = 'F{g'
        str_5 = 'Y:Fm'
        str_6 = '^e]'
        str_7 = module_0.remove_whitespace(str_5)
        colorama_printer_0 = module_0.ColoramaPrinter()
        colorama_printer_0.diff_line(str_4)
        bool_0 = True
        basic_printer_0 = module_0.BasicPrinter()
        bool_1 = False
        var_0 = module_0.create_terminal_printer(bool_0)
        path_0 = None
        text_i_o_0 = module_2.TextIO()
        text_i_o_1 = text_i_o_0.__enter__()
        str_8 = "l,~Z'-czFx8/7"
        var_1 = module_0.show_unified_diff(file_input=str_8, file_output=str_6, file_path=path_0, color_output=bool_1)
        str_9 = '--skip-glob'
        bool_2 = module_0.ask_whether_to_apply_changes_to_file(str_9)
    except BaseException:
        pass