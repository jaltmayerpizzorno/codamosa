# Automatically generated by Pynguin.
import httpie.output.formatters.json as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'format_options'
    str_1 = 'json'
    str_2 = 'format'
    str_3 = 'indent'
    str_4 = 'sort_keys'
    bool_0 = False
    var_0 = None
    var_1 = {str_2: bool_0, str_3: var_0, str_4: bool_0}
    var_2 = {str_1: var_1}
    var_3 = {str_0: var_2}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_3)

def test_case_2():
    str_0 = 'explicit_json'
    str_1 = 'format_options'
    bool_0 = False
    str_2 = 'json'
    str_3 = 'format'
    str_4 = 'indent'
    int_0 = 2
    var_0 = {str_3: bool_0, str_4: int_0, str_3: bool_0}
    var_1 = {str_2: var_0}
    var_2 = {str_0: bool_0, str_1: var_1}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
    str_5 = 'text'
    str_6 = j_s_o_n_formatter_0.format_body(str_0, str_5)
    str_7 = j_s_o_n_formatter_0.format_body(str_0, str_2)

def test_case_3():
    str_0 = 'Test method format_body of class JSONFormatter'
    str_1 = 'explicit_json'
    str_2 = 'format_options'
    bool_0 = False
    str_3 = 'json'
    str_4 = 'format'
    str_5 = 'indent'
    str_6 = 'sort_keys'
    int_0 = 2
    var_0 = {str_4: bool_0, str_5: int_0, str_6: bool_0}
    var_1 = {str_3: var_0}
    var_2 = {str_1: bool_0, str_2: var_1}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
    str_7 = '{"test": 1}'
    str_8 = 'application/json'
    str_9 = j_s_o_n_formatter_0.format_body(str_7, str_8)
    str_10 = 'w2WPW}/t}@7[[Z'
    str_11 = j_s_o_n_formatter_0.format_body(str_10, str_0)
    str_12 = j_s_o_n_formatter_0.format_body(str_3, str_9)

def test_case_4():
    str_0 = 'explicit_json'
    str_1 = 'format_options'
    bool_0 = False
    str_2 = 'json'
    str_3 = 'format'
    str_4 = 'indent'
    str_5 = 'sort_keys'
    int_0 = 2
    var_0 = {str_3: bool_0, str_4: int_0, str_5: bool_0}
    var_1 = {str_2: var_0}
    var_2 = {str_0: bool_0, str_1: var_1}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
    str_6 = 'BK:3zt\r'
    str_7 = 'Called just before the HTTP request is sent.\n\n        Might alter `request_headers`.\n\n        '
    str_8 = j_s_o_n_formatter_0.format_body(str_6, str_7)