# Automatically generated by Pynguin.
import ansible.parsing.utils.addresses as module_0

def test_case_0():
    try:
        bytes_0 = b"\xb4n'W\xa6\x03\x14\xa2\x8dd\xc3\xb7\\\x13;"
        var_0 = module_0.parse_address(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '9\\\t;y<!h{19M\x0bQ>V'
        var_0 = module_0.parse_address(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'dmsetup'
        float_0 = None
        var_0 = module_0.parse_address(str_0, float_0)
        bytes_0 = b'M\x12\xcd\xf8\xa5\xd0\x99H\xc1\x9d\xa2\xcf`\xeb\xb9\xea\x03'
        var_1 = module_0.parse_address(bytes_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'openbsd'
        set_0 = {str_0, str_0}
        var_0 = module_0.parse_address(str_0, set_0)
        str_1 = 'XJ/`BJ\\4E@'
        var_1 = module_0.parse_address(str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'host'
        var_0 = module_0.parse_address(str_0)
        str_1 = '192.168.1.1:1234'
        var_1 = module_0.parse_address(str_1)
        str_2 = '192.168.1.1'
        var_2 = module_0.parse_address(str_2)
        str_3 = '192.168.1.1[1:3]:1234'
        var_3 = module_0.parse_address(str_3)
    except BaseException:
        pass