# Automatically generated by Pynguin.
import ansible.plugins.inventory.constructed as module_0

def test_case_0():
    try:
        inventory_module_0 = module_0.InventoryModule()
        set_0 = {inventory_module_0, inventory_module_0, inventory_module_0}
        str_0 = "&;eKX.KP\tD@\nRt3C('"
        tuple_0 = (set_0, str_0)
        inventory_module_1 = module_0.InventoryModule()
        var_0 = inventory_module_1.get_all_host_vars(inventory_module_0, tuple_0, inventory_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n        Starts the command and communicates with it until it ends.\n        '
        str_1 = 'iu]&[ [0!w<P6%'
        bool_0 = False
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.host_groupvars(str_0, str_1, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'w>;Q"\'%\n)F^W;*&_*'
        int_0 = -2489
        inventory_module_0 = module_0.InventoryModule()
        inventory_module_1 = module_0.InventoryModule()
        var_0 = inventory_module_1.host_vars(str_0, int_0, inventory_module_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 2673.7692
        str_0 = 'baE[u.eEt?'
        tuple_0 = (str_0,)
        float_1 = 2337.698
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(float_0, tuple_0, float_1, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'z\x87\x1a'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        inventory_module_0 = None
        inventory_module_1 = module_0.InventoryModule()
        list_0 = [inventory_module_1, dict_0]
        inventory_module_2 = module_0.InventoryModule()
        var_0 = inventory_module_2.verify_file(list_0)
        var_1 = inventory_module_1.verify_file(inventory_module_0)
        inventory_module_3 = module_0.InventoryModule()
        bool_0 = False
        str_0 = ',t<x:2O#g*|WObQt'
        var_2 = inventory_module_3.parse(bytes_0, bool_0, str_0)
    except BaseException:
        pass