# Automatically generated by Pynguin.
import isort.format as module_0
import typing as module_1

def test_case_0():
    basic_printer_0 = module_0.BasicPrinter()

def test_case_1():
    str_0 = '_Ed('
    str_1 = module_0.format_simplified(str_0)

def test_case_2():
    str_0 = 'N>$aLcX}Fk\rV6R!\r%d'
    str_1 = module_0.format_natural(str_0)

def test_case_3():
    str_0 = ''
    basic_printer_0 = module_0.BasicPrinter()
    basic_printer_0.success(str_0)
    str_1 = module_0.format_natural(str_0)

def test_case_4():
    str_0 = '\rgR[Gpx5V1ky>'
    basic_printer_0 = module_0.BasicPrinter()
    basic_printer_0.error(str_0)

def test_case_5():
    str_0 = 'GiL\n5v&Z&lyg'
    text_i_o_0 = module_1.TextIO()
    text_i_o_1 = text_i_o_0.__enter__()
    basic_printer_0 = module_0.BasicPrinter(text_i_o_1)
    basic_printer_0.diff_line(str_0)

def test_case_6():
    colorama_printer_0 = module_0.ColoramaPrinter()

def test_case_7():
    str_0 = 'encodings'
    colorama_printer_0 = module_0.ColoramaPrinter()
    str_1 = colorama_printer_0.style_text(str_0)

def test_case_8():
    bool_0 = False
    var_0 = module_0.create_terminal_printer(bool_0)

def test_case_9():
    bool_0 = True
    var_0 = module_0.create_terminal_printer(bool_0)