# Automatically generated by Pynguin.
import ansible.plugins.inventory.yaml as module_0

def test_case_0():
    try:
        str_0 = 'Invalid conditional detected: %s'
        dict_0 = {str_0: str_0, str_0: str_0}
        str_1 = ''
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(str_0, dict_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        bytes_0 = None
        var_0 = inventory_module_0.verify_file(bytes_0)
        list_0 = []
        int_0 = -12
        inventory_module_1 = module_0.InventoryModule()
        var_1 = inventory_module_1.parse(inventory_module_0, list_0, inventory_module_0, int_0)
    except BaseException:
        pass