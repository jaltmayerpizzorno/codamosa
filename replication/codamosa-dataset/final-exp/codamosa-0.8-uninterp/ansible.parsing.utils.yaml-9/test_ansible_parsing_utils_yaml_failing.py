# Automatically generated by Pynguin.
import ansible.parsing.utils.yaml as module_0

def test_case_0():
    try:
        str_0 = '\n        ---\n        # We are ignoring the json value as it is not important right now.\n        # yaml version is the only one we care about.\n        ansible_variable:\n          yaml:\n            json: junk\n            yaml: success\n    '
        var_0 = module_0.from_yaml(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 2263
        var_0 = module_0.from_yaml(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\r\xca\x17\x1b\x01\x04G\xd8 \xa6jSe\xbe\x1e\xd1l\xbd'
        var_0 = module_0.from_yaml(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 0.5
        complex_0 = None
        float_1 = None
        bool_0 = False
        bytes_0 = b'\xa7\xdcz\xb59K\xeb\xb6\\\x02\xa50W'
        var_0 = module_0.from_yaml(float_0, complex_0, float_1, bool_0, bytes_0)
    except BaseException:
        pass