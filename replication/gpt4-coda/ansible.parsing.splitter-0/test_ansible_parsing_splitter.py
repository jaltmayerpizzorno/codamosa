# Automatically generated by Pynguin.
import ansible.parsing.splitter as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '> a\n\x0bVNIBmz<G7mE+y\t'
    var_0 = module_0.parse_kv(str_0)

def test_case_2():
    str_0 = 'key1=value1 key2=\'value with spaces\' key3="value with quotes"'
    var_0 = module_0.parse_kv(str_0)

def test_case_3():
    str_0 = 'key1=value1 key2=value2'
    bool_0 = True
    var_0 = module_0.parse_kv(str_0, bool_0)

def test_case_4():
    str_0 = ''
    var_0 = module_0.parse_kv(str_0, str_0)

def test_case_5():
    str_0 = 'Accepts a dict or list of dicts, and a dotted accessor and produces a product\n    of the element and the results of the dotted accessor\n\n    >>> obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]\n    >>> subelements(obj, \'groups\')\n    [({\'name\': \'alice\', \'groups\': [\'wheel\'], \'authorized\': [\'/tmp/alice/onekey.pub\']}, \'wheel\')]\n\n    '
    var_0 = module_0.parse_kv(str_0)

def test_case_6():
    dict_0 = {}
    var_0 = module_0.join_args(dict_0)

def test_case_7():
    bytes_0 = None
    var_0 = module_0.parse_kv(bytes_0)
    dict_0 = {}
    var_1 = module_0.join_args(dict_0)

def test_case_8():
    str_0 = '\\'
    var_0 = module_0.parse_kv(str_0, str_0)
    var_1 = module_0.parse_kv(str_0)