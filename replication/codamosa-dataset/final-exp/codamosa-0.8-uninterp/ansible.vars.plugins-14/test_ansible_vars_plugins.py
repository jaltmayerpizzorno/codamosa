# Automatically generated by Pynguin.
import ansible.vars.plugins as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'B\x98mS\xcb]p:\xc2Z\xd2\x15'
    float_0 = 2748.0
    list_0 = []
    tuple_0 = ()
    var_0 = module_0.get_plugin_vars(bytes_0, float_0, list_0, tuple_0)

def test_case_2():
    str_0 = 'inventory'
    var_0 = module_0.get_vars_from_path(str_0, str_0, str_0, str_0)

def test_case_3():
    str_0 = "bZd,4'l"
    bool_0 = True
    list_0 = []
    var_0 = module_0.get_vars_from_inventory_sources(bool_0, str_0, list_0, str_0)