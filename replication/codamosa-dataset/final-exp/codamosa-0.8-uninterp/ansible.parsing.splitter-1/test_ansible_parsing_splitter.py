# Automatically generated by Pynguin.
import ansible.parsing.splitter as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xcf19\xcd'
    var_0 = module_0.parse_kv(bytes_0)

def test_case_2():
    str_0 = 'Ek10<QZE*B "1fxsq)I'
    var_0 = module_0.join_args(str_0)

def test_case_3():
    str_0 = '<    do\tker_extra_args="--log-opt max-size=10m --log-opd max-file=3"\n    '
    var_0 = module_0.parse_kv(str_0)

def test_case_4():
    str_0 = 'o*H#1-;\nxY'
    var_0 = module_0.parse_kv(str_0)

def test_case_5():
    str_0 = '([PF_,Y\tI\nM, WY?|j'
    set_0 = {str_0, str_0}
    var_0 = module_0.parse_kv(str_0, set_0)
    var_1 = module_0.join_args(str_0)
    bytes_0 = None
    var_2 = module_0.parse_kv(bytes_0)

def test_case_6():
    str_0 = 'a=foo b= bar c="{{test}}" d= baz'
    var_0 = module_0.parse_kv(str_0)

def test_case_7():
    str_0 = 'name=test arg="a 1"'
    var_0 = module_0.parse_kv(str_0)
    bool_0 = True
    var_1 = module_0.parse_kv(str_0, bool_0)
    str_1 = 'name=test arg="a \'1\'" b=test'
    var_2 = module_0.parse_kv(str_1)

def test_case_8():
    str_0 = 'T-a=;|sll3)h|r'
    var_0 = module_0.parse_kv(str_0)

def test_case_9():
    str_0 = ')6j\r!\\Y%}'
    var_0 = module_0.parse_kv(str_0)

def test_case_10():
    str_0 = 'a=b c="foo bar"\nd=e f="g h"'
    var_0 = module_0.split_args(str_0)
    str_1 = 'key=value \\\nk2=v2'
    var_1 = module_0.split_args(str_1)

def test_case_11():
    str_0 = 'a=foo b="bar" c="{{test}}" d="baz"'
    bool_0 = True
    var_0 = module_0.parse_kv(str_0, bool_0)

def test_case_12():
    str_0 = 'a=foo \\= bar c="{{test}}" d= baz'
    str_1 = 'r.?5osE'
    list_0 = [str_1, str_1, str_0, str_1]
    tuple_0 = (list_0,)
    var_0 = module_0.parse_kv(str_0, tuple_0)