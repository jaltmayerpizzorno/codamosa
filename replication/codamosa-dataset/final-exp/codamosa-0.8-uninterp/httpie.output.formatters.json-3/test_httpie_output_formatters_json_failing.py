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
        str_4 = 'indent'
        bool_1 = True
        int_0 = 2
        var_0 = {str_3: bool_1, int_0: bool_1, str_2: bool_1, str_4: int_0}
        var_1 = {str_2: var_0}
        var_2 = {str_0: bool_0, str_1: var_1}
        j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
        str_5 = 'y[yHb'
        str_6 = 'u\t0\rP"zN&DP\n{vJ'
        str_7 = j_s_o_n_formatter_0.format_body(str_5, str_6)
        str_8 = None
        str_9 = j_s_o_n_formatter_0.format_body(str_8, str_8)
    except BaseException:
        pass