# Automatically generated by Pynguin.
import httpie.output.formatters.json as module_0

def test_case_0():
    try:
        j_s_o_n_formatter_0 = module_0.JSONFormatter()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'format_options'
        str_1 = 'explicit_json'
        str_2 = 'json'
        str_3 = 'format'
        str_4 = 'sort_keys'
        bool_0 = True
        int_0 = 27
        var_0 = {str_3: bool_0, str_1: int_0, str_4: bool_0}
        var_1 = {str_2: var_0}
        bool_1 = False
        var_2 = {str_0: var_1, str_1: bool_1}
        j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
        str_5 = 'N\rj29J'
        str_6 = j_s_o_n_formatter_0.format_body(str_5, str_3)
        str_7 = "I'/O<f\tq&lVQ"
        str_8 = 'json.sot_keys:true'
        str_9 = j_s_o_n_formatter_0.format_body(str_7, str_8)
        j_s_o_n_formatter_1 = module_0.JSONFormatter()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'format_options'
        str_1 = 'explicit_json'
        str_2 = 'json'
        str_3 = 'format'
        str_4 = 'indent'
        str_5 = 'sort_keys'
        bool_0 = True
        int_0 = 27
        var_0 = {str_3: bool_0, str_4: int_0, str_5: bool_0}
        var_1 = {str_2: var_0}
        bool_1 = True
        var_2 = {str_0: var_1, str_1: bool_1}
        j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
        str_6 = "JcL$:;_q{7'lp\\ \t"
        str_7 = j_s_o_n_formatter_0.format_body(str_5, str_6)
        str_8 = 'B!U|XI/jFI##Hv:}yU '
        str_9 = '`M%8in*'
        str_10 = j_s_o_n_formatter_0.format_body(str_8, str_9)
        str_11 = j_s_o_n_formatter_0.format_body(str_5, str_2)
        str_12 = ':~XmZu<\x0chK0Y0\t.CpL'
        str_13 = j_s_o_n_formatter_0.format_body(str_2, str_12)
        j_s_o_n_formatter_1 = module_0.JSONFormatter()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'format_options'
        str_1 = 'explicit_json'
        str_2 = 'json'
        str_3 = 'format'
        str_4 = 'indent'
        str_5 = 'sort_keys'
        bool_0 = True
        int_0 = 27
        var_0 = {str_3: bool_0, str_4: int_0, str_5: bool_0}
        var_1 = {str_2: var_0}
        bool_1 = True
        var_2 = {str_0: var_1, str_1: bool_1}
        j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
        str_6 = "JcL$:;_q{7'lp\\ \t"
        str_7 = j_s_o_n_formatter_0.format_body(str_5, str_6)
        str_8 = '\tTE%}y. '
        str_9 = j_s_o_n_formatter_0.format_body(str_6, str_8)
        str_10 = None
        str_11 = 'Ul$iDz#_j6W'
        str_12 = j_s_o_n_formatter_0.format_body(str_10, str_11)
    except BaseException:
        pass