# Automatically generated by Pynguin.
import ansible.plugins.inventory.toml as module_0

def test_case_0():
    try:
        bytes_0 = b'A\xa0\x06\xc3nB\xeaya\r/\x99/J\xa2\xd9\xd2\xe4'
        list_0 = [bytes_0, bytes_0, bytes_0]
        var_0 = module_0.toml_dumps(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        bytes_0 = b'\xf9\x10\xcc\\\xc5'
        var_0 = inventory_module_0.parse(bytes_0, inventory_module_0, bytes_0)
    except BaseException:
        pass