# Automatically generated by Pynguin.
import ansible.plugins.inventory.auto as module_0

def test_case_0():
    try:
        inventory_module_0 = module_0.InventoryModule()
        inventory_module_1 = module_0.InventoryModule()
        var_0 = inventory_module_1.verify_file(inventory_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = None
        str_0 = '\\8ciE>I@vx\r(<yID*YQ'
        int_0 = 684
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(bytes_0, str_0, int_0)
    except BaseException:
        pass