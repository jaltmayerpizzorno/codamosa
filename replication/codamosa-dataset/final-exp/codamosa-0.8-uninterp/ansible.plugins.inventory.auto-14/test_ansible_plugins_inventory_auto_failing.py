# Automatically generated by Pynguin.
import ansible.plugins.inventory.auto as module_0

def test_case_0():
    try:
        float_0 = -2066.84
        bytes_0 = b"\x0c{y\x9bEQ\x9d\x7f\xc84N\xa2q{n'EO\x18"
        float_1 = -48.9
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(float_0, bytes_0, float_1)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        str_0 = '/tmp/test.yml'
        var_0 = inventory_module_0.verify_file(str_0)
        var_1 = inventory_module_0.verify_file(inventory_module_0)
    except BaseException:
        pass