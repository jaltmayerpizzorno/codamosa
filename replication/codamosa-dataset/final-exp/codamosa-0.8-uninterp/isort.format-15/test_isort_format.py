# Automatically generated by Pynguin.
import isort.format as module_0
import pathlib as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    str_0 = '>9a/[" \'1ym"l%['
    str_1 = module_0.format_simplified(str_0)
    var_0 = module_0.create_terminal_printer(bool_0)

def test_case_2():
    str_0 = 'nP.\t\nMf:3[^j"r&'
    str_1 = module_0.format_natural(str_0)

def test_case_3():
    str_0 = 'H{\r1\r2Yc^2(` 7fa(g9S'
    str_1 = module_0.format_natural(str_0)

def test_case_4():
    str_0 = 'R'
    colorama_printer_0 = module_0.ColoramaPrinter()
    str_1 = 'Tells isort to follow symlinks that are encountered when running recursively.'
    colorama_printer_0.diff_line(str_1)
    colorama_printer_0.diff_line(str_1)
    str_2 = colorama_printer_0.style_text(str_0)
    str_3 = '"_D`~04\n{.'
    str_4 = colorama_printer_0.style_text(str_3)
    str_5 = colorama_printer_0.style_text(str_3)
    str_6 = module_0.format_natural(str_3)
    str_7 = module_0.format_natural(str_6)
    colorama_printer_1 = module_0.ColoramaPrinter()
    colorama_printer_1.diff_line(str_2)
    str_8 = 'import('
    str_9 = colorama_printer_1.style_text(str_8, str_2)
    dict_0 = {}
    path_0 = module_1.Path(**dict_0)
    str_10 = ')"Ie$hY'
    var_0 = module_0.show_unified_diff(file_input=str_4, file_output=str_10, file_path=path_0)

def test_case_5():
    str_0 = 'Fixing '
    set_0 = None
    bytes_0 = b'\x88\xd7\x19K\xfb\xf9\xe2>Iz\x05G\xd1\xfb\xff\r]\xae\xb7\x16'
    bool_0 = True
    var_0 = module_0.show_unified_diff(file_input=str_0, file_output=str_0, file_path=set_0, output=bytes_0, color_output=bool_0)
    basic_printer_0 = module_0.BasicPrinter()
    bool_1 = True
    var_1 = module_0.create_terminal_printer(bool_1)

def test_case_6():
    str_0 = '2oYejV<)5,X'
    str_1 = module_0.remove_whitespace(str_0)

def test_case_7():
    float_0 = None
    colorama_printer_0 = module_0.ColoramaPrinter(float_0)

def test_case_8():
    str_0 = ',@dNPG(\t`|`=?Y=t#Gp{'
    basic_printer_0 = module_0.BasicPrinter()
    basic_printer_0.diff_line(str_0)

def test_case_9():
    str_0 = 'dataclasses'
    colorama_printer_0 = module_0.ColoramaPrinter()
    str_1 = colorama_printer_0.style_text(str_0)
    str_2 = 'T'
    basic_printer_0 = module_0.BasicPrinter()
    basic_printer_1 = module_0.BasicPrinter()
    str_3 = 'v@LZ"? :?'
    str_4 = module_0.remove_whitespace(str_3)
    basic_printer_1.success(str_2)

def test_case_10():
    str_0 = '-#Qn{3"'
    colorama_printer_0 = module_0.ColoramaPrinter()
    str_1 = "_*[*N'X}?\rw."
    colorama_printer_0.diff_line(str_0)
    str_2 = colorama_printer_0.style_text(str_1)
    str_3 = "'@-\tBd+#{J"
    str_4 = module_0.format_natural(str_3)
    str_5 = 'X'
    colorama_printer_0.diff_line(str_5)
    str_6 = 'HU-E\tpiQoy0,8\x0b=>3(3g'
    str_7 = colorama_printer_0.style_text(str_6)
    colorama_printer_0.diff_line(str_1)
    str_8 = module_0.format_simplified(str_0)
    basic_printer_0 = module_0.BasicPrinter()
    bool_0 = True
    var_0 = module_0.create_terminal_printer(bool_0)

def test_case_11():
    str_0 = '-#Qn{3"'
    colorama_printer_0 = module_0.ColoramaPrinter()
    str_1 = "_*[*N'X}?\rw."
    colorama_printer_0.diff_line(str_0)
    str_2 = colorama_printer_0.style_text(str_1)
    str_3 = "'@-\tBd+#{J"
    str_4 = module_0.format_natural(str_3)
    str_5 = 'X'
    colorama_printer_0.diff_line(str_5)
    str_6 = 'HU-E\tpiQoy0,8\x0b=>3(3g'
    str_7 = colorama_printer_0.style_text(str_6)
    colorama_printer_0.diff_line(str_1)
    str_8 = module_0.format_simplified(str_0)
    str_9 = '+1#+3{z'
    str_10 = 'CR|fPehWp\ns$frKL>KH{'
    str_11 = colorama_printer_0.style_text(str_10, str_2)
    str_12 = colorama_printer_0.style_text(str_5, str_9)
    colorama_printer_0.diff_line(str_9)
    basic_printer_0 = module_0.BasicPrinter()
    str_13 = '/<PX:tI]}d%'
    basic_printer_0.success(str_13)
    basic_printer_0.error(str_13)

def test_case_12():
    bool_0 = True
    var_0 = module_0.create_terminal_printer(bool_0)

def test_case_13():
    bool_0 = None
    var_0 = module_0.create_terminal_printer(bool_0)