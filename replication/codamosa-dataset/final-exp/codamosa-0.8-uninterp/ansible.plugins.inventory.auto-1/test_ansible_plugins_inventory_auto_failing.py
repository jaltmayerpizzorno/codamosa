# Automatically generated by Pynguin.
import ansible.plugins.inventory.auto as module_0

def test_case_0():
    try:
        bytes_0 = b'\xe2\xe8\xc4\x85\xb8\x96M\x00\x1dz\xd7:\xf1'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\re\t/s&]'
        dict_0 = {str_0: str_0, str_0: str_0}
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(str_0, dict_0, dict_0)
    except BaseException:
        pass