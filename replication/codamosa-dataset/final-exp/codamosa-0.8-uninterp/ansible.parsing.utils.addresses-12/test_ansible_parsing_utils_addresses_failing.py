# Automatically generated by Pynguin.
import ansible.parsing.utils.addresses as module_0

def test_case_0():
    try:
        str_0 = '94YmR"ge8It>jN]DV'
        var_0 = module_0.parse_address(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '192.168.0.1'
        var_0 = module_0.parse_address(str_0)
        str_1 = '192.168.0.1:123'
        var_1 = module_0.parse_address(str_1)
        str_2 = '192.168.0.1[1:3]'
        var_2 = module_0.parse_address(str_2)
    except BaseException:
        pass