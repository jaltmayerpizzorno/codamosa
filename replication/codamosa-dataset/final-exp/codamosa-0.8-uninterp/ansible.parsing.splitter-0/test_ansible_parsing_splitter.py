# Automatically generated by Pynguin.
import ansible.parsing.splitter as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'I8\xef\x8d\xc7@\x18'
    var_0 = module_0.parse_kv(bytes_0)

def test_case_2():
    tuple_0 = None
    var_0 = module_0.parse_kv(tuple_0)

def test_case_3():
    str_0 = 'disable batch mode for sshpass'
    var_0 = module_0.split_args(str_0)

def test_case_4():
    str_0 = "-(tr+.`\x0bA\r:\t\x0c'wC7I"
    var_0 = module_0.join_args(str_0)

def test_case_5():
    str_0 = '#9BX00lL\ng3OP)3S\x0cNpO'
    var_0 = module_0.split_args(str_0)

def test_case_6():
    bool_0 = False
    str_0 = 'blah="foo bar" bletch=\'{"a":1}\' zoinks={"a":1}'
    var_0 = module_0.parse_kv(str_0, bool_0)

def test_case_7():
    str_0 = 'K$%I!=m|\nG'
    var_0 = module_0.parse_kv(str_0)
    str_1 = '=8bVQ~}iS'
    var_1 = module_0.parse_kv(str_1)
    var_2 = module_0.parse_kv(str_0, str_0)

def test_case_8():
    str_0 = '=4ULX:_'
    var_0 = module_0.parse_kv(str_0)

def test_case_9():
    bool_0 = True
    str_0 = 'blah="fo ba?" letch=\'{"a":1}\' zoinks={"a":1%'
    var_0 = module_0.parse_kv(str_0, bool_0)

def test_case_10():
    str_0 = 'creates=/tmp/foo executable=/bin/bash remov es=/tmp/bar'
    bool_0 = True
    var_0 = module_0.parse_kv(str_0, bool_0)
    str_1 = 'spam={{ pig }} ham={{ cox }}'
    var_1 = module_0.parse_kv(str_1, bool_0)

def test_case_11():
    str_0 = 'baz {{ test }} "testing more" \n more \n testing \n {% endif %} '
    var_0 = module_0.split_args(str_0)

def test_case_12():
    str_0 = '\\'
    var_0 = module_0.parse_kv(str_0)