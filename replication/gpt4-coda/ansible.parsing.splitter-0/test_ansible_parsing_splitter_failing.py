# Automatically generated by Pynguin.
import ansible.parsing.splitter as module_0

def test_case_0():
    try:
        list_0 = []
        var_0 = module_0.parse_kv(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ";L'6U\x0bIl=x_7"
        var_0 = module_0.parse_kv(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 15
        var_0 = module_0.split_args(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\x0c6#Rblb"0\']-\'$^pM9?\\'
        var_0 = module_0.parse_kv(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'Accepts a dict or list of dicts, and a dotted accessor and produces a product\n9   of the element and the results of the dotted accessor\n\n    >>> obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]\n    >>> subelements(obj, \'groups\')\n    [({\'name\': ialice\', \'groups\': [\'wheel\'], \'authorized\': [\'/tmp/alice/onekey.pub\']}, \'wheel\')]\n\n    '
        var_0 = module_0.parse_kv(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '\nlxPrQ)P3FcHoE]1;)bA'
        var_0 = module_0.parse_kv(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '*2YR!Nw\x0b8j)UGB\\aT'
        var_0 = module_0.parse_kv(str_0)
        str_1 = 'Custom iterencode, primarily design to handle encoding ``AnsibleUnsafe``\n        as the ``AnsibleUnsafe`` subclasses inherit from string types and\n        ``json.JSONEncoder`` does not support custom encoders for string types\n        '
        var_1 = module_0.split_args(str_1)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'P&?u7:4C@)[Ty}@#}'
        var_0 = module_0.parse_kv(str_0)
        str_1 = '\r\r^hkT'
        var_1 = module_0.split_args(str_1)
        float_0 = 1.5
        str_2 = '9XN[^%H\x0cq=<O3C7c\\H'
        tuple_0 = (float_0, str_2)
        str_3 = 'E/1'
        bool_0 = True
        list_0 = [tuple_0, str_3, str_3, bool_0]
        var_2 = module_0.parse_kv(list_0)
    except BaseException:
        pass