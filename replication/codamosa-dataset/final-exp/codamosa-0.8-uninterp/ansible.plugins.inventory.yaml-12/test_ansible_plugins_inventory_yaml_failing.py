# Automatically generated by Pynguin.
import ansible.plugins.inventory.yaml as module_0

def test_case_0():
    try:
        bool_0 = True
        int_0 = 1844
        list_0 = [int_0, bool_0]
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(bool_0, int_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        str_0 = '/bin'
        var_0 = inventory_module_0.verify_file(str_0)
        tuple_0 = None
        list_0 = []
        var_1 = inventory_module_0.parse(tuple_0, list_0, inventory_module_0, str_0)
    except BaseException:
        pass