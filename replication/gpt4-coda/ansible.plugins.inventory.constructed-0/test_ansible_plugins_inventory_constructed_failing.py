# Automatically generated by Pynguin.
import ansible.plugins.inventory.constructed as module_0

def test_case_0():
    try:
        str_0 = "become_prompt: (source=%s, state=%s): '%s'"
        set_0 = {str_0, str_0}
        bytes_0 = b'?\xc08/\nC\x07\x9dmu5OFE\x0e\xbex33'
        tuple_0 = (bytes_0,)
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.get_all_host_vars(str_0, set_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        str_0 = 'deprecated'
        float_0 = -138.0
        str_1 = 'Hj$X: ARMs1 o-gZ6:|'
        var_0 = inventory_module_0.host_groupvars(str_0, float_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_module_0 = module_0.InventoryModule()
        bytes_0 = b'tQCO\xe9,+\x9ehz\xeb\xfas\xb5\xc8\xaf\xe9a\x1b\xc7'
        dict_0 = {}
        var_0 = inventory_module_0.host_vars(bytes_0, dict_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Qv[x)WAHKpila\x0b -&"kw'
        list_0 = [str_0, str_0, str_0]
        bytes_0 = b','
        tuple_0 = (str_0, bytes_0)
        float_0 = 3201.945401
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(list_0, tuple_0, float_0, tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '+EhO!xWuo!X<\x0b'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(str_0)
        inventory_module_1 = module_0.InventoryModule()
        int_0 = 24
        bool_0 = False
        list_0 = [inventory_module_1, inventory_module_0, str_0]
        var_1 = inventory_module_0.parse(int_0, bool_0, list_0, list_0)
    except BaseException:
        pass