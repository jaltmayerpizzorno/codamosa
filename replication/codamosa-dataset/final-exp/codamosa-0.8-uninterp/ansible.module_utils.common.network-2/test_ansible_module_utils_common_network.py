# Automatically generated by Pynguin.
import ansible.module_utils.common.network as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '255.255.w255.256'
    var_0 = module_0.is_netmask(str_0)

def test_case_2():
    float_0 = 1267.5
    var_0 = module_0.is_netmask(float_0)

def test_case_3():
    float_0 = 842.5316552131872
    str_0 = ';'
    set_0 = {str_0, str_0, float_0, str_0}
    str_1 = 'E\x0byxX(QpRWHr&1eluE'
    tuple_0 = (set_0, str_1)
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.is_netmask(list_0)
    var_1 = module_0.to_netmask(var_0)

def test_case_4():
    str_0 = '192.168.100.10'
    str_1 = '255.255.255.0'
    var_0 = module_0.to_subnet(str_0, str_1)
    str_2 = '24'
    var_1 = module_0.to_subnet(str_0, str_2)
    bool_0 = True
    var_2 = module_0.to_subnet(str_0, str_1, bool_0)
    var_3 = module_0.to_subnet(str_0, str_2, bool_0)

def test_case_5():
    str_0 = 'xXd+wHM)3M'
    var_0 = module_0.to_ipv6_network(str_0)

def test_case_6():
    str_0 = '255.255.255.0'
    var_0 = module_0.to_bits(str_0)

def test_case_7():
    str_0 = '2Nj1Ylgs\x0c_v~Cg'
    var_0 = module_0.is_mac(str_0)

def test_case_8():
    str_0 = 'xXd+wHM)3M'
    var_0 = module_0.to_ipv6_network(str_0)
    var_1 = module_0.to_ipv6_subnet(str_0)

def test_case_9():
    str_0 = '255.255.255.256'
    var_0 = module_0.is_netmask(str_0)
    bool_0 = False
    var_1 = module_0.to_subnet(str_0, bool_0)

def test_case_10():
    str_0 = '2515.255.w255.256'
    var_0 = module_0.is_netmask(str_0)

def test_case_11():
    str_0 = '0.0.0.0'
    var_0 = module_0.to_masklen(str_0)
    str_1 = '255.255.255.255'
    var_1 = module_0.to_masklen(str_1)

def test_case_12():
    str_0 = '2001:db8:85a3:8d3:1319:8a2e:370:7348'
    var_0 = module_0.to_ipv6_network(str_0)
    str_1 = '2001:db8:85a3:8d3:1319:8a2e:370::'
    var_1 = module_0.to_ipv6_network(str_1)
    str_2 = '2001:db8:85a3:8d3:1319:8a2e::'
    var_2 = module_0.to_ipv6_network(str_2)
    str_3 = '2001:db8:85a3:8d3:1319::'
    var_3 = module_0.to_ipv6_network(str_3)