# Automatically generated by Pynguin.
import ansible.module_utils.common.network as module_0

def test_case_0():
    try:
        set_0 = None
        var_0 = module_0.to_bits(set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = None
        var_0 = module_0.to_masklen(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'bj+D!Plx#twflyJ|v '
        var_0 = module_0.to_netmask(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 2586.406
        str_0 = '\x0c$=cu,YAa}*'
        var_0 = module_0.to_subnet(float_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '=\\aub/\x0b\\a:'
        bool_0 = True
        var_0 = module_0.to_netmask(bool_0)
        var_1 = module_0.to_ipv6_subnet(str_0)
        var_2 = module_0.to_subnet(str_0, var_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '=\\aub/\x0b\\a:'
        var_0 = module_0.to_ipv6_network(str_0)
        bool_0 = True
        var_1 = module_0.to_netmask(bool_0)
        var_2 = module_0.to_ipv6_subnet(str_0)
        var_3 = module_0.to_subnet(var_0, var_1)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = []
        var_0 = module_0.to_ipv6_network(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = ()
        var_0 = module_0.is_masklen(tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '<)N'
        var_0 = module_0.to_ipv6_network(str_0)
        int_0 = -4013
        var_1 = module_0.to_ipv6_subnet(str_0)
        var_2 = module_0.to_subnet(var_0, int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = []
        var_0 = module_0.to_subnet(list_0, list_0)
    except BaseException:
        pass