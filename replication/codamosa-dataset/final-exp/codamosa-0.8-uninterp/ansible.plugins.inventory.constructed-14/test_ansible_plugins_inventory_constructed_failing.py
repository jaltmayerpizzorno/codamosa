# Automatically generated by Pynguin.
import ansible.plugins.inventory.constructed as module_0

def test_case_0():
    try:
        inventory_module_0 = module_0.InventoryModule()
        list_0 = []
        int_0 = 3600
        str_0 = 'i|wYn]'
        var_0 = inventory_module_0.get_all_host_vars(list_0, int_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b''
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        bytes_1 = b'\x9f:\xb0+\x17<\xcd\xbb\xb9\xddsVH\xfe'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.host_vars(set_0, set_0, bytes_1)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        inventory_module_0 = None
        str_0 = '<|X'
        inventory_module_1 = module_0.InventoryModule()
        var_0 = inventory_module_1.parse(bool_0, inventory_module_0, str_0)
    except BaseException:
        pass