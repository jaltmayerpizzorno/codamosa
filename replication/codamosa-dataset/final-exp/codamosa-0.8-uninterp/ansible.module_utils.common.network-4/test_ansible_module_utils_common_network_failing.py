# Automatically generated by Pynguin.
import ansible.module_utils.common.network as module_0

def test_case_0():
    try:
        tuple_0 = None
        var_0 = module_0.to_masklen(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '192.168.1.5'
        var_0 = module_0.to_subnet(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        var_0 = module_0.to_netmask(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -849.2644511818442
        var_0 = module_0.to_netmask(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = None
        var_0 = module_0.to_ipv6_subnet(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '/\nhd&MnTzp~+w,z78'
        var_0 = module_0.to_bits(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = -531
        var_0 = module_0.is_mac(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0}
        var_0 = module_0.to_subnet(bool_0, set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '192.168.0.1'
        str_1 = '24'
        var_0 = module_0.to_subnet(str_0, str_1)
        str_2 = '255.255.255.0'
        var_1 = module_0.to_subnet(str_0, str_2)
        bool_0 = True
        var_2 = module_0.to_subnet(str_0, str_1, bool_0)
        bool_1 = False
        var_3 = module_0.to_bits(bool_1)
    except BaseException:
        pass