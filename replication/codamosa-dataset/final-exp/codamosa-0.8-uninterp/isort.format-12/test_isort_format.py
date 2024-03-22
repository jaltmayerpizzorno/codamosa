# Automatically generated by Pynguin.
import isort.format as module_0
import typing as module_1

def test_case_0():
    basic_printer_0 = module_0.BasicPrinter()

def test_case_1():
    str_0 = '@x'
    str_1 = module_0.format_simplified(str_0)

def test_case_2():
    str_0 = ' but was given a literal of type '
    str_1 = module_0.format_natural(str_0)

def test_case_3():
    str_0 = 'import a'
    str_1 = module_0.format_natural(str_0)
    str_2 = 'from a import b'
    str_3 = module_0.format_natural(str_2)
    str_4 = 'a.b'
    str_5 = module_0.format_natural(str_4)
    str_6 = 'a.b.c'
    str_7 = module_0.format_natural(str_6)
    str_8 = 'a.b.c.d'
    str_9 = module_0.format_natural(str_8)

def test_case_4():
    str_0 = 'yiwIAAu~N#$HK3h*vy\x0c$'
    str_1 = module_0.format_simplified(str_0)
    basic_printer_0 = module_0.BasicPrinter()
    str_2 = None
    basic_printer_0.success(str_2)
    basic_printer_1 = module_0.BasicPrinter()
    str_3 = 'u\rh@l0Bx\ny`E6'
    basic_printer_0.error(str_3)
    basic_printer_1.diff_line(str_3)
    str_4 = module_0.remove_whitespace(str_3)

def test_case_5():
    str_0 = 'Ci 4p,'
    basic_printer_0 = module_0.BasicPrinter()
    basic_printer_0.error(str_0)
    basic_printer_1 = module_0.BasicPrinter()

def test_case_6():
    str_0 = "oCP4E+dl 4&N'n%"
    str_1 = module_0.format_simplified(str_0)
    basic_printer_0 = module_0.BasicPrinter()
    basic_printer_0.diff_line(str_0)

def test_case_7():
    colorama_printer_0 = module_0.ColoramaPrinter()

def test_case_8():
    str_0 = 'lcw{`fklz83aA],'
    colorama_printer_0 = module_0.ColoramaPrinter()
    str_1 = colorama_printer_0.style_text(str_0)

def test_case_9():
    str_0 = 'RU067%Y:Rt%-kh.^8L'
    dict_0 = {}
    colorama_printer_0 = module_0.ColoramaPrinter(dict_0)
    colorama_printer_0.diff_line(str_0)

def test_case_10():
    bool_0 = True
    var_0 = module_0.create_terminal_printer(bool_0)

def test_case_11():
    str_0 = '(f2WvfyP6b}!U0'
    dict_0 = {}
    text_i_o_0 = module_1.TextIO(**dict_0)
    colorama_printer_0 = module_0.ColoramaPrinter(text_i_o_0)
    colorama_printer_0.diff_line(str_0)

def test_case_12():
    bool_0 = None
    var_0 = module_0.create_terminal_printer(bool_0)
    str_0 = 'x5w&'
    str_1 = module_0.format_simplified(str_0)
    basic_printer_0 = module_0.BasicPrinter()
    str_2 = 'settings'
    basic_printer_0.diff_line(str_2)
    str_3 = 'M8zbvb+BB0R5'
    str_4 = module_0.format_simplified(str_3)

def test_case_13():
    str_0 = 'from example1 import  example2'
    str_1 = module_0.format_simplified(str_0)

def test_case_14():
    str_0 = 'import os,sys'
    str_1 = module_0.format_simplified(str_0)