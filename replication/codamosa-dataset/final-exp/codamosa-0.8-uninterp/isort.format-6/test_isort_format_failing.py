# Automatically generated by Pynguin.
import pathlib as module_0
import isort.format as module_1
import typing as module_2

def test_case_0():
    try:
        str_0 = 'py_version'
        list_0 = [str_0, str_0]
        path_0 = module_0.Path(*list_0)
        var_0 = module_1.show_unified_diff(file_input=str_0, file_output=str_0, file_path=path_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'SC&,_"#re$e'
        basic_printer_0 = module_1.BasicPrinter()
        basic_printer_0.success(str_0)
        str_1 = module_1.remove_whitespace(str_0, str_0)
        str_2 = 'tB\x0cgH\\Y4$L=&AvywC"\n'
        str_3 = module_1.format_natural(str_2)
        path_0 = module_0.Path()
        var_0 = module_1.show_unified_diff(file_input=str_1, file_output=str_1, file_path=path_0)
        bool_0 = module_1.ask_whether_to_apply_changes_to_file(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'test.tt'
        bool_0 = module_1.ask_whether_to_apply_changes_to_file(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'AVzM'
        str_1 = module_1.remove_whitespace(str_0)
        str_2 = '+1!"ME='
        bool_0 = module_1.ask_whether_to_apply_changes_to_file(str_2)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\x0cKuW'
        str_1 = '~Ajx6V}3tub7f U<1'
        str_2 = '4^'
        list_0 = [str_0, str_1, str_0]
        basic_printer_0 = module_1.BasicPrinter(list_0)
        basic_printer_0.success(str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        var_0 = module_1.create_terminal_printer(bool_0)
        str_0 = 'i9'
        bool_1 = module_1.ask_whether_to_apply_changes_to_file(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'mb@(F8}<-ozz'
        colorama_printer_0 = module_1.ColoramaPrinter()
        str_1 = colorama_printer_0.style_text(str_0)
        colorama_printer_0.diff_line(str_0)
        str_2 = None
        basic_printer_0 = module_1.BasicPrinter()
        basic_printer_0.success(str_2)
        str_3 = module_1.remove_whitespace(str_1)
        str_4 = ''
        str_5 = module_1.format_natural(str_4)
        dict_0 = {str_0: str_2}
        path_0 = module_0.Path(**dict_0)
        str_6 = 'as '
        bool_0 = True
        var_0 = module_1.show_unified_diff(file_input=str_6, file_output=str_1, file_path=path_0, color_output=bool_0)
        str_7 = 'quHh3m'
        bool_1 = module_1.ask_whether_to_apply_changes_to_file(str_7)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'U1yjWz'
        colorama_printer_0 = module_1.ColoramaPrinter()
        basic_printer_0 = module_1.BasicPrinter()
        basic_printer_0.success(str_0)
        str_1 = module_1.format_natural(str_0)
        str_2 = 'i!d['
        colorama_printer_1 = module_1.ColoramaPrinter()
        str_3 = colorama_printer_1.style_text(str_2)
        str_4 = '__init__.py'
        colorama_printer_1.diff_line(str_4)
        str_5 = 'Trying8to sort using an undefined sort_type. Defined sort types are '
        str_6 = module_1.format_simplified(str_5)
        bool_0 = False
        var_0 = module_1.create_terminal_printer(bool_0)
        str_7 = '+L'
        str_8 = module_1.format_natural(str_1)
        list_0 = [str_2]
        path_0 = module_0.Path(*list_0)
        str_9 = 'Z[={v>u@'
        var_1 = module_1.show_unified_diff(file_input=str_7, file_output=str_9, file_path=path_0, color_output=bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        colorama_printer_0 = module_1.ColoramaPrinter()
        str_0 = 'i!d['
        str_1 = colorama_printer_0.style_text(str_0)
        str_2 = 'Trying to sort using an undefined sort_type. Defined sort types are '
        str_3 = module_1.format_simplified(str_2)
        bool_0 = True
        var_0 = module_1.create_terminal_printer(bool_0)
        str_4 = module_1.format_natural(str_2)
        str_5 = module_1.format_natural(str_4)
        bool_1 = True
        var_1 = module_1.create_terminal_printer(bool_1)
        colorama_printer_1 = module_1.ColoramaPrinter()
        str_6 = '%}(g95,zta\x0cBC9_+}'
        text_i_o_0 = module_2.TextIO()
        basic_printer_0 = module_1.BasicPrinter(text_i_o_0)
        basic_printer_0.success(str_6)
        str_7 = "!eDuIi\\,HD^|8kt'>D="
        str_8 = colorama_printer_0.style_text(str_7)
        bool_2 = module_1.ask_whether_to_apply_changes_to_file(str_3)
    except BaseException:
        pass