# Automatically generated by Pynguin.
import ansible.parsing.splitter as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xf7T\r\x00)\xe4\xea\xbb\x1d_\xa4J\x9b\x81\\'
    var_0 = module_0.parse_kv(bytes_0)

def test_case_2():
    str_0 = 'a=b c="d e"'
    var_0 = module_0.parse_kv(str_0)

def test_case_3():
    str_0 = '&as2Xp!-'
    var_0 = module_0.join_args(str_0)

def test_case_4():
    dict_0 = None
    var_0 = module_0.parse_kv(dict_0)

def test_case_5():
    str_0 = ''
    var_0 = module_0.parse_kv(str_0)

def test_case_6():
    str_0 = ''
    var_0 = module_0.split_args(str_0)

def test_case_7():
    str_0 = '=) d e'
    var_0 = module_0.join_args(str_0)
    var_1 = module_0.parse_kv(str_0)

def test_case_8():
    str_0 = 'ls -ltr \\\n/tmp \\\n|| ls -ltr /opt || echo "I like trains"'
    var_0 = module_0.split_args(str_0)

def test_case_9():
    str_0 = '!fTSegI\nKm`:NJ&i}(u'
    var_0 = module_0.parse_kv(str_0)

def test_case_10():
    str_0 = 'a=b c="d e"'
    bool_0 = True
    var_0 = module_0.parse_kv(str_0, bool_0)

def test_case_11():
    str_0 = 'key1=value1 key2="value 2" "key 3"="value 3" "key 4"="value 4" "with backslash"=\\"value 5'
    var_0 = module_0.parse_kv(str_0)

def test_case_12():
    str_0 = '{% abc %} = "cd\\"f"'
    var_0 = module_0.split_args(str_0)