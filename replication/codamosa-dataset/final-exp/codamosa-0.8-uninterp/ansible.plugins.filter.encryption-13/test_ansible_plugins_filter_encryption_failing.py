# Automatically generated by Pynguin.
import ansible.plugins.filter.encryption as module_0

def test_case_0():
    try:
        str_0 = ''
        var_0 = module_0.do_vault(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Z'
        bool_0 = True
        float_0 = 1120.303
        list_0 = [str_0, bool_0, float_0, str_0]
        var_0 = module_0.do_vault(str_0, bool_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = None
        set_0 = set()
        tuple_0 = (list_0, set_0)
        str_0 = 'backports.ssl_match_hostname'
        bytes_0 = None
        var_0 = module_0.do_vault(tuple_0, str_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "+\x0c7<T7e0g]6Om^8'C"
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        filter_module_1 = module_0.FilterModule()
        var_1 = filter_module_0.filters()
        bool_0 = True
        var_2 = module_0.do_unvault(str_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = None
        str_0 = '\x0caT0jS\x0bCQ$\x0bD|1`'
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.do_unvault(dict_0, str_0, filter_module_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '$ANSIBLE_VAULT;1.1;AES256;test_default'
        var_0 = module_0.do_unvault(str_0, str_0)
    except BaseException:
        pass