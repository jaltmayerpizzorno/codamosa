# Automatically generated by Pynguin.
import ansible.module_utils.common.network as module_0

def test_case_0():
    int_0 = 1593
    var_0 = module_0.is_masklen(int_0)

def test_case_1():
    bool_0 = True
    var_0 = module_0.to_netmask(bool_0)
    str_0 = '255.255.255.0'
    var_1 = module_0.to_bits(str_0)

def test_case_2():
    str_0 = '192.168.1.1'
    str_1 = '24'
    var_0 = module_0.to_subnet(str_0, str_1)
    str_2 = '255.255.255.0'
    var_1 = module_0.to_subnet(str_0, str_2)
    str_3 = '255.255.0.0'
    bool_0 = True
    var_2 = module_0.to_subnet(str_0, str_3, bool_0)

def test_case_3():
    str_0 = '1}(~o~A:[\x0c~(\nIjC*b'
    var_0 = module_0.to_ipv6_subnet(str_0)

def test_case_4():
    str_0 = 'j{RlfYW\t`'
    var_0 = module_0.is_mac(str_0)

def test_case_5():
    str_0 = '255.255.255.10'
    var_0 = module_0.is_netmask(str_0)

def test_case_6():
    str_0 = '255.255.255.0'
    var_0 = module_0.to_bits(str_0)

def test_case_7():
    str_0 = '255.255.255.0'
    var_0 = module_0.is_netmask(str_0)
    str_1 = '255.255.255.10'
    var_1 = module_0.is_netmask(str_1)

def test_case_8():
    bool_0 = True
    var_0 = module_0.to_netmask(bool_0)
    var_1 = module_0.to_subnet(var_0, var_0)

def test_case_9():
    str_0 = '::'
    var_0 = module_0.to_ipv6_network(str_0)
    str_1 = '::1'
    var_1 = module_0.to_ipv6_network(str_1)
    str_2 = '1::'
    var_2 = module_0.to_ipv6_network(str_2)
    str_3 = '1::1'
    var_3 = module_0.to_ipv6_network(str_3)
    str_4 = '1:2:3:4:5::'
    var_4 = module_0.to_ipv6_network(str_4)
    str_5 = '1:2:3:4:5::6'
    var_5 = module_0.to_ipv6_network(str_5)

def test_case_10():
    str_0 = '2001:db8:1:2:3:4:5:6'
    var_0 = module_0.to_ipv6_subnet(str_0)