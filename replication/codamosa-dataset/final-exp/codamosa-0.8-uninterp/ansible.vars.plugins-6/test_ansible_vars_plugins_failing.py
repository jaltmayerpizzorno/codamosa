# Automatically generated by Pynguin.
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

def test_case_0():
    try:
        var_0 = None
        var_1 = module_0.get_vars_from_path(var_0, var_0, var_0, var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'w(X^sE/>9\x0cV0'
        dict_0 = {str_0: str_0, str_0: str_0}
        var_0 = module_0.get_plugin_vars(str_0, str_0, dict_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "#Ph'"
        bytes_0 = b'T\xab'
        var_0 = module_0.get_vars_from_inventory_sources(str_0, str_0, str_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        complex_0 = None
        int_0 = -2806
        bool_0 = True
        var_0 = module_0.get_plugin_vars(complex_0, int_0, bool_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 348.96
        set_0 = set()
        list_0 = [float_0]
        str_0 = 'inventory'
        var_0 = module_0.get_vars_from_path(float_0, set_0, list_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ",|f:+yoKd0$5dR*'zn("
        bytes_0 = b'>\x98?k)\xf2I\xfe\xc8'
        var_0 = module_0.get_vars_from_inventory_sources(str_0, str_0, str_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        tuple_0 = None
        dict_0 = {tuple_0: tuple_0}
        set_0 = set()
        bool_0 = False
        var_0 = module_0.get_vars_from_inventory_sources(tuple_0, dict_0, set_0, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = set()
        host_0 = module_1.Host()
        float_0 = -1972.1
        list_0 = [host_0]
        var_0 = module_0.get_vars_from_path(host_0, float_0, list_0, set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '/4\n502lBFw\rC?&P:3'
        bytes_0 = b'\xc5\x8c\xd7jN]\x9a\xb9@\x0b7\xad'
        var_0 = module_0.get_vars_from_inventory_sources(str_0, str_0, str_0, bytes_0)
    except BaseException:
        pass