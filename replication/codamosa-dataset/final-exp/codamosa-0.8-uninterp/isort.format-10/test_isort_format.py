# Automatically generated by Pynguin.
import isort.format as module_0
import typing as module_1
import pathlib as module_2

def test_case_0():
    colorama_printer_0 = module_0.ColoramaPrinter()

def test_case_1():
    str_0 = 'Yts),oC:uyG\n'
    str_1 = module_0.format_simplified(str_0)

def test_case_2():
    str_0 = "2e;$Y^2,\r3Z:S)o'"
    str_1 = module_0.format_natural(str_0)

def test_case_3():
    str_0 = ']A ZR\t)vu'
    str_1 = module_0.remove_whitespace(str_0)

def test_case_4():
    str_0 = 'v|P5{9yZvY'
    str_1 = module_0.format_natural(str_0)
    str_2 = "+5MPI11_#'@JGW!6;C"
    basic_printer_0 = module_0.BasicPrinter()
    basic_printer_0.error(str_2)

def test_case_5():
    str_0 = '-ot'
    basic_printer_0 = module_0.BasicPrinter()
    basic_printer_0.diff_line(str_0)
    dict_0 = {}
    text_i_o_0 = module_1.TextIO(**dict_0)
    colorama_printer_0 = module_0.ColoramaPrinter(text_i_o_0)

def test_case_6():
    str_0 = 'A!D^mFGU |BZ#B'
    colorama_printer_0 = module_0.ColoramaPrinter()
    list_0 = [colorama_printer_0]
    basic_printer_0 = module_0.BasicPrinter(list_0)
    colorama_printer_0.diff_line(str_0)

def test_case_7():
    bool_0 = True
    var_0 = module_0.create_terminal_printer(bool_0)

def test_case_8():
    str_0 = 'from . import (A, B)'
    str_1 = module_0.format_natural(str_0)
    bool_0 = True
    var_0 = module_0.create_terminal_printer(bool_0)
    str_2 = 'import datetime as dt, json'
    str_3 = module_0.format_natural(str_2)

def test_case_9():
    str_0 = '\n?Q~'
    str_1 = 'honor_case_in_force_sorted_sections'
    optional_0 = None
    bool_0 = True
    var_0 = module_0.show_unified_diff(file_input=str_0, file_output=str_1, file_path=optional_0, color_output=bool_0)
    colorama_printer_0 = module_0.ColoramaPrinter()
    text_i_o_0 = module_1.TextIO()
    colorama_printer_0.diff_line(str_0)
    str_2 = '\\wQ\t#K'
    str_3 = colorama_printer_0.style_text(str_2)
    str_4 = '@zrtNC66_u&d*'
    str_5 = module_0.format_natural(str_4)
    basic_printer_0 = module_0.BasicPrinter(text_i_o_0)
    basic_printer_0.error(str_1)
    str_6 = 'h]&3\n`>Gw'
    str_7 = module_0.format_simplified(str_5)
    basic_printer_1 = module_0.BasicPrinter()
    basic_printer_0.success(str_6)
    str_8 = colorama_printer_0.style_text(str_0)
    str_9 = '/C"Au/R(t:R'
    path_0 = module_2.Path()
    var_1 = module_0.show_unified_diff(file_input=str_0, file_output=str_9, file_path=path_0)
    basic_printer_1.success(str_1)