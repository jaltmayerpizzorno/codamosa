# Automatically generated by Pynguin.
import httpie.output.formatters.json as module_0
import json as module_1

def test_case_0():
    str_0 = 'explicit_json'
    str_1 = 'format_options'
    bool_0 = False
    str_2 = 'json'
    str_3 = 'format'
    str_4 = 'sort_keys'
    str_5 = 'indent'
    int_0 = 4
    var_0 = {str_3: bool_0, str_4: bool_0, str_5: int_0}
    var_1 = {str_2: var_0}
    var_2 = {str_0: bool_0, str_1: var_1}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)

def test_case_1():
    str_0 = 'json'
    bool_0 = False
    var_0 = None
    str_1 = 'explicit_json'
    str_2 = 'format_options'
    str_3 = 'json'
    str_4 = 'format'
    str_5 = 'inde>nt'
    str_6 = 'sort_keys'
    bool_1 = True
    var_1 = {str_4: bool_1, str_5: var_0, str_6: bool_1}
    var_2 = {str_3: var_1}
    var_3 = {str_1: bool_0, str_2: var_2}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_3)
    str_7 = j_s_o_n_formatter_0.format_body(str_5, str_0)

def test_case_2():
    str_0 = 'format_options'
    str_1 = 'explicit_json'
    str_2 = 'json'
    str_3 = 'format'
    bool_0 = True
    int_0 = 4
    var_0 = {str_3: bool_0, str_3: int_0, str_3: bool_0}
    var_1 = {str_2: var_0}
    bool_1 = True
    var_2 = {str_0: var_1, str_1: bool_1}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
    str_4 = 'name'
    str_5 = 'age'
    str_6 = 'is_teacher'
    str_7 = 'address'
    int_1 = 31
    str_8 = j_s_o_n_formatter_0.format_body(str_5, str_3)
    var_3 = {str_4: str_4, str_5: int_1, str_6: bool_1, str_7: str_7}
    str_9 = 'application/json'
    str_10 = j_s_o_n_formatter_0.format_body(str_8, str_9)
    var_4 = module_1.dumps(var_3, indent=int_0, sort_keys=bool_0)