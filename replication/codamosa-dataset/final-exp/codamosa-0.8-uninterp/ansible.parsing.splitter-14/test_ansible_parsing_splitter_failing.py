# Automatically generated by Pynguin.
import ansible.parsing.splitter as module_0

def test_case_0():
    try:
        bool_0 = False
        var_0 = module_0.parse_kv(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 2319.6261
        var_0 = module_0.join_args(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "1(3'q6$"
        var_0 = module_0.parse_kv(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'v\n\'h5I5rTs-BJW]"'
        var_0 = module_0.parse_kv(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\n    Unit test for fuction parse_kv\n    '
        str_1 = 'k1=v1 k2=v2'
        var_0 = module_0.parse_kv(str_1)
        var_1 = module_0.parse_kv(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'k1=v k2==v2 $3="v3 k="v 4" "k5=v5"'
        var_0 = module_0.parse_kv(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '$}}\r}~#_RTQxG?tUK":'
        bool_0 = True
        var_0 = module_0.parse_kv(str_0, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '\\'
        list_0 = [str_0, str_0, str_0]
        var_0 = module_0.join_args(list_0)
        var_1 = module_0.parse_kv(str_0)
        set_0 = None
        var_2 = module_0.split_args(set_0)
    except BaseException:
        pass