# Automatically generated by Pynguin.
import ansible.module_utils.common.network as module_0

def test_case_0():
    str_0 = '255.255.255.0'
    var_0 = module_0.is_netmask(str_0)

def test_case_1():
    str_0 = '112.168.1.1'
    bool_0 = True
    int_0 = 313
    var_0 = module_0.to_subnet(str_0, bool_0, int_0)

def test_case_2():
    str_0 = '255.255.255.0'
    var_0 = module_0.to_subnet(str_0, str_0)

def test_case_3():
    int_0 = -286
    var_0 = module_0.is_masklen(int_0)

def test_case_4():
    str_0 = 'nh\\\nEzTAt s\\'
    var_0 = module_0.to_ipv6_subnet(str_0)

def test_case_5():
    str_0 = 'M}"s9}xvmW\x0c\t'
    var_0 = module_0.to_ipv6_network(str_0)

def test_case_6():
    str_0 = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    var_0 = module_0.to_ipv6_network(str_0)

def test_case_7():
    str_0 = '192.168.1.1'
    var_0 = module_0.is_netmask(str_0)

def test_case_8():
    str_0 = '255.255.255.0'
    var_0 = module_0.to_masklen(str_0)

def test_case_9():
    str_0 = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    var_0 = module_0.to_ipv6_subnet(str_0)

def test_case_10():
    str_0 = '255.255.255.0'
    var_0 = module_0.to_bits(str_0)