# Automatically generated by Pynguin.
import ansible.module_utils.common.network as module_0

def test_case_0():
    try:
        str_0 = '&:{=tA'
        bool_0 = True
        var_0 = module_0.is_netmask(bool_0)
        var_1 = module_0.to_ipv6_subnet(str_0)
        bool_1 = True
        var_2 = module_0.to_netmask(bool_1)
        list_0 = []
        var_3 = module_0.to_bits(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -179.5
        var_0 = module_0.to_netmask(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '(H_AKNH(Z\nyHC7T'
        var_0 = module_0.to_subnet(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 2908.0
        list_0 = [float_0]
        var_0 = module_0.to_ipv6_network(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = ()
        var_0 = module_0.to_bits(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '5=!/op\\GoAdZ[eVb1'
        bool_0 = True
        var_0 = module_0.is_netmask(bool_0)
        var_1 = module_0.to_ipv6_subnet(str_0)
        list_0 = [var_0, var_0, var_1, var_1]
        var_2 = module_0.is_masklen(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'dPefw5+\nHofW'
        int_0 = -875
        var_0 = module_0.to_subnet(str_0, int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '2001:0db8:85a3:08d3:1319:8a2e:0370:7344'
        var_0 = module_0.to_ipv6_network(str_0)
        bool_0 = True
        tuple_0 = ()
        bytes_0 = b'\xdd\xc5&\xdf/&\xce\xa3\xb8\x8exg\x0b\x95\xd6\xe2U'
        var_1 = module_0.to_subnet(bool_0, tuple_0, bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '192.168.1.1'
        str_1 = '255.255.255.0'
        var_0 = module_0.to_subnet(str_0, str_1)
        str_2 = '24'
        var_1 = module_0.to_subnet(str_0, str_2)
        bool_0 = True
        var_2 = module_0.to_subnet(str_0, str_2, bool_0)
        str_3 = '2001:db8:aaa:bbbb::1'
        str_4 = '64'
        var_3 = module_0.to_subnet(str_3, str_4)
    except BaseException:
        pass