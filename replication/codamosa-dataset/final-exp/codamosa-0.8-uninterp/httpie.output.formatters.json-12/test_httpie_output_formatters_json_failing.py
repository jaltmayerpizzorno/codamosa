# Automatically generated by Pynguin.
import httpie.output.formatters.json as module_0

def test_case_0():
    try:
        j_s_o_n_formatter_0 = module_0.JSONFormatter()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'explicit_json'
        str_1 = 'format_options'
        bool_0 = True
        str_2 = 'json'
        str_3 = 'format'
        bool_1 = {str_3: bool_0}
        bool_2 = {str_2: bool_1}
        bool_3 = {str_0: bool_0, str_1: bool_2}
        j_s_o_n_formatter_0 = module_0.JSONFormatter(**bool_3)
        str_4 = None
        str_5 = j_s_o_n_formatter_0.format_body(str_4, str_2)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'explicit_json'
        str_1 = 'format_options'
        bool_0 = False
        str_2 = 'json'
        str_3 = 'format'
        bool_1 = {str_3: bool_0}
        bool_2 = {str_2: bool_1}
        bool_3 = {str_0: bool_0, str_1: bool_2}
        j_s_o_n_formatter_0 = module_0.JSONFormatter(**bool_3)
        str_4 = None
        str_5 = '\n        Sorts headers by name while retaining relative\n        order of multiple headers with the same name.\n\n        '
        str_6 = j_s_o_n_formatter_0.format_body(str_5, str_4)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'explicit_json'
        str_1 = 'format_options'
        bool_0 = True
        str_2 = 'json'
        str_3 = 'format'
        bool_1 = {str_3: bool_0}
        bool_2 = {str_2: bool_1}
        bool_3 = {str_0: bool_0, str_1: bool_2}
        j_s_o_n_formatter_0 = module_0.JSONFormatter(**bool_3)
        str_4 = '1.0'
        str_5 = " <o5rwgk 'a[L <"
        str_6 = j_s_o_n_formatter_0.format_body(str_4, str_5)
    except BaseException:
        pass