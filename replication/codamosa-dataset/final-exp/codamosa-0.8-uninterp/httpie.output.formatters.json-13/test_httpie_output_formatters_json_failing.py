# Automatically generated by Pynguin.
import httpie.output.formatters.json as module_0

def test_case_0():
    try:
        j_s_o_n_formatter_0 = module_0.JSONFormatter()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        str_0 = 'format_options'
        str_1 = 'json'
        str_2 = 'sort_keys'
        str_3 = 'indent'
        bool_1 = True
        int_0 = 4
        var_0 = {str_2: bool_1, str_3: int_0}
        var_1 = {str_1: var_0}
        var_2 = {str_0: var_1}
        j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'json'
        str_1 = 'colors'
        str_2 = 'style'
        str_3 = 'format'
        str_4 = 'sot_eys'
        bool_0 = True
        int_0 = -317
        var_0 = {str_3: bool_0, str_3: int_0, str_4: bool_0}
        var_1 = {}
        str_5 = 'headers'
        str_6 = 'none'
        str_7 = {str_5: str_6}
        var_2 = {str_0: var_0, str_1: var_1, str_2: str_7}
        str_8 = 'explicit_json'
        str_9 = 'format_options'
        var_3 = {str_8: bool_0, str_9: var_2}
        j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_3)
        str_10 = None
        str_11 = ',_>'
        str_12 = j_s_o_n_formatter_0.format_body(str_10, str_11)
    except BaseException:
        pass