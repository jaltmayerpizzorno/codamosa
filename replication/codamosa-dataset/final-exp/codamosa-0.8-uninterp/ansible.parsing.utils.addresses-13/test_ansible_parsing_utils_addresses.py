# Automatically generated by Pynguin.
import ansible.parsing.utils.addresses as module_0

def test_case_0():
    str_0 = 'unicode'
    var_0 = module_0.parse_address(str_0)

def test_case_1():
    str_0 = '2'
    int_0 = -1815
    var_0 = module_0.parse_address(str_0, int_0)

def test_case_2():
    str_0 = '192.0.2.1:80'
    var_0 = module_0.parse_address(str_0)
    str_1 = '192.0.2.1:8080'
    var_1 = module_0.parse_address(str_1)