# Automatically generated by Pynguin.
import ansible.plugins.inventory.auto as module_0

def test_case_0():
    try:
        str_0 = 'hw.logicalcpu'
        set_0 = {str_0, str_0, str_0, str_0}
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x9f\x9cARK\x1eh\xc4t\xcbr\x9b\xffAR\r\x9f\xf9'
        list_0 = [bytes_0, bytes_0, bytes_0]
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(bytes_0, bytes_0, list_0)
    except BaseException:
        pass