# Automatically generated by Pynguin.
import ansible.module_utils.common.network as module_0

def test_case_0():
    try:
        bool_0 = True
        var_0 = module_0.is_mac(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        var_0 = module_0.to_netmask(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '(>Nr<z9h)aw#u'
        var_0 = module_0.to_subnet(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 3487
        var_0 = module_0.to_netmask(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -6140.14494
        var_0 = module_0.to_masklen(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 32600
        var_0 = module_0.to_ipv6_subnet(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        var_0 = module_0.to_ipv6_network(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '%r'
        var_0 = module_0.to_ipv6_network(str_0)
        var_1 = module_0.is_netmask(str_0)
        bool_0 = True
        tuple_0 = ()
        bytes_0 = b'\xe9C\xfc\xefC\x97\x81\x13\xda\x0b\xa9N\x96\xb8P\x17P\xf5'
        float_0 = -842.0956
        tuple_1 = (tuple_0, bytes_0, float_0, bool_0)
        float_1 = -1054.005
        var_2 = module_0.to_subnet(tuple_1, float_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = None
        var_0 = module_0.is_netmask(str_0)
        str_1 = 'J:9O\x0bl,)'
        list_0 = [str_1]
        var_1 = module_0.to_subnet(str_1, list_0)
    except BaseException:
        pass